# Local exports — mostly ignored by Git

Place local renders and downloads in this directory, one folder per shot (for example `demo-d01-sh03/`). `.gitignore` excludes everything here except this README.

**Exception — golden videos in Git LFS (showrunner, 2026-11-23):** the takes the showrunner selected, and the current cut, are committed with Git LFS at their named path (`<shot>/<shot>-<take>.mp4`), added with `git add -f`. Everything else (rejected takes, Flow's originally named duplicates, WAVs, contact sheets, older cuts) stays local. See [spec/production-pipeline.md](../../spec/production-pipeline.md#file-naming-and-storage).

Keep durable copies, checksums, and production-storage locations in manifests outside ephemeral workstations.
