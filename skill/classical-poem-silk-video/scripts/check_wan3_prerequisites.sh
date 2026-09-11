#!/usr/bin/env bash
set -euo pipefail

failed=0

require_command() {
  if command -v "$1" >/dev/null 2>&1; then
    printf 'ok   command %s\n' "$1"
  else
    printf 'fail command %s\n' "$1" >&2
    failed=1
  fi
}

for command_name in python ffmpeg ffprobe rg; do
  require_command "$command_name"
done

if python -c "import dashscope" >/dev/null 2>&1; then
  printf 'ok   Python package dashscope\n'
else
  printf 'fail Python package dashscope\n' >&2
  failed=1
fi

if [ -n "${DASHSCOPE_API_KEY:-}" ]; then
  printf 'ok   DASHSCOPE_API_KEY is set\n'
else
  printf 'fail DASHSCOPE_API_KEY is not set\n' >&2
  failed=1
fi

if [ -n "${DASHSCOPE_BASE_URL:-}" ]; then
  printf 'ok   DASHSCOPE_BASE_URL is set\n'
else
  printf 'fail DASHSCOPE_BASE_URL is not set\n' >&2
  failed=1
fi

exit "$failed"
