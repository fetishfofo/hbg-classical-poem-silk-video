#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <workspace-image> <prompt-file> <output-relative-to-outputs/wan3>" >&2
  exit 2
fi

skill_dir="$(cd "$(dirname "$0")" && pwd)"
workspace="$(pwd)"
image="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
prompt_file="$2"
output_rel="$3"

case "$image" in
  "$workspace"/*) ;;
  *)
    echo "Image must be inside the current workspace: $workspace" >&2
    exit 2
    ;;
esac

case "$output_rel" in
  /*|*..*)
    echo "Output must be a safe relative path" >&2
    exit 2
    ;;
esac

if [ ! -f "$prompt_file" ]; then
  echo "Prompt file not found: $prompt_file" >&2
  exit 2
fi

if [ -z "${DASHSCOPE_API_KEY:-}" ]; then
  echo "DASHSCOPE_API_KEY is not set" >&2
  exit 2
fi

if [ -z "${DASHSCOPE_BASE_URL:-}" ]; then
  echo "DASHSCOPE_BASE_URL is not set" >&2
  exit 2
fi

prompt="$(<"$prompt_file")"
output="$workspace/outputs/wan3/$output_rel"

mkdir -p "$output"

POEM_I2V_IMAGE="$image" \
POEM_I2V_OUTPUT="$output" \
POEM_I2V_PROMPT="$prompt" \
python "$skill_dir/wan3_i2v.py"

echo "$output"
