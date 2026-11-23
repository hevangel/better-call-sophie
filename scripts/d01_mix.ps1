# Mix the D01 commercial with ffmpeg (traditional tools only).
# Picture: the 25 s cut, then 5 s of the exterior plate. Dialogue: each shot's own audio.
# Bed: 25 s of the instrumental take, ducked under the dialogue (sidechaincompress).
# Tag: the sung "Better call Sophie!" placed so its chord ends before 30 s. Master: loudnorm -14 LUFS.
#
# Mix v01 (approved 2026-11-23) was made with:
#   ./scripts/d01_mix.ps1 -Bed production/exports/demo-d01-jingle/demo-d01-jingle-v02.mp3 -BedStart 1.85 `
#     -Tag production/exports/demo-d01-jingle/demo-d01-jingle-tag-v01.mp3 -TagStart 0 -TagLen 3.6 -TagAt 26.2 `
#     -Out production/exports/demo-d01-mix/demo-d01-mix-v01.mp4
# Needs ffmpeg on PATH (libopenh264 is used because the WinGet build has no libx264).
param([Parameter(Mandatory)] [string]$Bed, [double]$BedStart = 0, [Parameter(Mandatory)] [string]$Tag, [double]$TagStart = 0, [double]$TagLen = 5, [double]$TagAt = 25,
      [string]$Cut = 'production/exports/demo-d01-roughcut/demo-d01-roughcut-v03.mp4', [Parameter(Mandatory)] [string]$Out)
$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)   # run from the repo root
$plate = 'assets/locations/sophie-office/office-exterior-dusk.webp'
$fc = @(
  # Picture: the 25 s cut, then 5 s of the exterior plate (end card text comes later).
  "[1:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,format=yuv420p,trim=duration=5,setpts=PTS-STARTPTS[plate]",
  "[0:v]fps=24,format=yuv420p,setsar=1[cut]",
  "[cut][plate]concat=n=2:v=1:a=0[v]",
  # Dialogue: the cut's own audio, padded to 30 s.
  "[0:a]aresample=48000,apad=whole_dur=30,asplit=2[dlg][key]",
  # Bed: 25 s from the bed take, fade in/out, ducked under the dialogue.
  "[2:a]aresample=48000,atrim=start=${BedStart}:duration=25,asetpts=PTS-STARTPTS,afade=t=in:d=0.3,afade=t=out:st=24.2:d=0.8,volume=0.55,apad=whole_dur=30[bed]",
  "[bed][key]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck]",
  # Tag: from the tag take, starting at 25 s.
  "[3:a]aresample=48000,atrim=start=${TagStart}:duration=${TagLen},asetpts=PTS-STARTPTS,afade=t=out:st=$($TagLen-0.4):d=0.4,adelay=$([int]($TagAt*1000))|$([int]($TagAt*1000)),apad=whole_dur=30[tag]",
  "[dlg][duck][tag]amix=inputs=3:normalize=0,atrim=duration=30,loudnorm=I=-14:TP=-1.5:LRA=11[a]"
) -join ';'
ffmpeg -v error -y -i $Cut -loop 1 -i $plate -i $Bed -i $Tag -filter_complex $fc -map '[v]' -map '[a]' -t 30 -c:v libopenh264 -b:v 8M -c:a aac -b:a 192k -ar 48000 $Out
ffprobe -v error -show_entries format=duration -of csv=p=0 $Out
ffmpeg -hide_banner -i $Out -af ebur128=framelog=quiet -f null - 2>&1 | Select-String 'I:\s+(-?[\d.]+) LUFS' | Select -Last 1 | % Line
