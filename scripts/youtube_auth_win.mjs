// Preload for running youtube-mcp's `youtube-auth` on Windows without patching the submodule.
//
// youtube-mcp v0.3.3 opens the sign-in link with `cmd /c start "" <url>`. cmd treats each `&`
// in the URL as a command separator, so Google receives a link cut after its first parameter
// ("Error 400: invalid_request, Required parameter is missing: response_type").
// This preload swaps that one call for `rundll32 url.dll,FileProtocolHandler <url>`, which
// passes the whole URL to the default browser, and also prints the URL as a fallback.
//
// Usage (from the repo root, with the env from ~/.config/youtube-mcp/env):
//   node --import ./scripts/youtube_auth_win.mjs external/youtube-mcp/dist/index.js youtube-auth

import childProcess from 'node:child_process';
import { syncBuiltinESMExports } from 'node:module';

const original = childProcess.spawn;
childProcess.spawn = function patchedSpawn(command, args, options) {
  if (command === 'cmd' && Array.isArray(args) && args[0] === '/c' && args[1] === 'start' && args[2] === '' && /^https:\/\/accounts\.google\.com\//.test(args[3] ?? '')) {
    const url = args[3];
    process.stderr.write(`Opening the Google sign-in page. If no browser opens, paste this link into one:\n${url}\n`);
    return original.call(this, 'rundll32', ['url.dll,FileProtocolHandler', url], options);
  }
  return original.call(this, command, args, options);
};
syncBuiltinESMExports();
