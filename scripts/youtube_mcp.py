"""Call one tool of the youtube-mcp server (external/youtube-mcp) from the command line.

The server is an MCP server; this script starts it over stdio, calls one tool, prints the JSON
result and exits. Its local state (OAuth token, approvals, upload sessions) lives in the state
directory, so a preflight, an approval and the write itself can be separate calls.

Settings come from a private env file outside the repo (default ~/.config/youtube-mcp/env,
KEY=VALUE lines): YOUTUBE_OAUTH_CLIENT_SECRET_FILE, YOUTUBE_MCP_PROFILE_ID,
YOUTUBE_MCP_CHANNEL_ID and optionally YOUTUBE_API_KEY and YOUTUBE_MCP_STATE_DIR.
Never put these values in the repo or in chat.

Usage (from the repo root, after `npm ci` in external/youtube-mcp):

    uv run --no-project --with mcp python scripts/youtube_mcp.py --list
    uv run --no-project --with mcp python scripts/youtube_mcp.py youtube_auth_status
    uv run --no-project --with mcp python scripts/youtube_mcp.py youtube_preflight_upload '{"filePath": "...", "title": "..."}'
    uv run --no-project --with mcp python scripts/youtube_mcp.py TOOL --args-file args.json

Every channel write is preflight, then youtube_approve, then the write with confirm: true.
Show the showrunner each preview and get their yes before approving it.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

REPO = Path(__file__).resolve().parent.parent
SERVER = REPO / "external" / "youtube-mcp" / "dist" / "index.js"
KEYS = ("YOUTUBE_API_KEY", "YOUTUBE_OAUTH_CLIENT_SECRET_FILE", "YOUTUBE_MCP_PROFILE_ID", "YOUTUBE_MCP_CHANNEL_ID", "YOUTUBE_MCP_STATE_DIR")


def load_env(path: Path) -> dict[str, str]:
    env = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k.strip() in KEYS:
            env[k.strip()] = v.strip()
    return env


async def run(tool: str | None, args: dict, env: dict[str, str]) -> None:
    params = StdioServerParameters(command="node", args=[str(SERVER), "--transport", "stdio"], env={**os.environ, **env})
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            if tool is None:
                for t in (await session.list_tools()).tools:
                    print(t.name)
                return
            result = await session.call_tool(tool, args)
            for item in result.content:
                text = getattr(item, "text", None)
                try:
                    print(json.dumps(json.loads(text), indent=2, ensure_ascii=False) if text else item)
                except (TypeError, ValueError):
                    print(text)
            if getattr(result, "is_error", None) or getattr(result, "isError", False):
                raise SystemExit(1)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tool", nargs="?")
    ap.add_argument("args", nargs="?", default="{}", help="tool arguments as JSON")
    ap.add_argument("--args-file", type=Path, help="read the tool arguments from a JSON file")
    ap.add_argument("--list", action="store_true", help="list the server's tools")
    ap.add_argument("--env-file", type=Path, default=Path.home() / ".config" / "youtube-mcp" / "env")
    a = ap.parse_args()
    if not SERVER.exists():
        raise SystemExit(f"{SERVER} is missing: run `npm ci` in external/youtube-mcp")
    env = load_env(a.env_file) if a.env_file.exists() else {}
    args = json.loads(a.args_file.read_text(encoding="utf-8")) if a.args_file else json.loads(a.args)
    asyncio.run(run(None if a.list else a.tool, args, env))


if __name__ == "__main__":
    main()
