# Runtime contract

Use this reference when preparing a machine for the skill or diagnosing the Wan 3.0 video-generation runtime.

## Host requirements

- Codex with the built-in `image_gen` tool for still-frame generation.
- Python 3 with the `dashscope` package installed.
- FFmpeg, ffprobe, and ripgrep.
- Alibaba Cloud Bailian access to the `wan3.0-video` model.
- `DASHSCOPE_API_KEY` set in the active environment.
- `DASHSCOPE_BASE_URL` set to the DashScope native API base URL for the same Bailian region and workspace as the API key.

Run `scripts/check_wan3_prerequisites.sh` from the active project before generating media.

## Wan 3.0 requirements

Video animation uses Alibaba Cloud Bailian Wan 3.0 through the DashScope API.

The skill passes each accepted local still frame to Wan 3.0 as a `first_frame` input. Local images are encoded as Base64 Data URIs by `scripts/wan3_i2v.py`, so a separate OSS upload step is not required for normal still-frame animation.

The video-generation stage uses:

- Model: `wan3.0-video`
- Python SDK: `dashscope`
- Wrapper: `scripts/wan3_i2v.sh`
- Generator: `scripts/wan3_i2v.py`
- Output directory: `outputs/wan3`

Generated video files are downloaded to the local workspace immediately after generation.

## Environment variables

Required:

    export DASHSCOPE_API_KEY="YOUR_API_KEY"
    export DASHSCOPE_BASE_URL="YOUR_DASHSCOPE_NATIVE_API_BASE_URL"

Never print, copy into project files, or commit the API key.

Optional video-generation settings:

    export POEM_I2V_RESOLUTION="720P"
    export POEM_I2V_DURATION="5"
    export POEM_I2V_RATIO="adaptive"

If these optional variables are not set, the Wan 3.0 wrapper uses its built-in defaults.

## Security and region rules

The API key, workspace endpoint, and Wan 3.0 model access must belong to compatible Alibaba Cloud Bailian configuration and region.

Do not store `DASHSCOPE_API_KEY` in `SKILL.md`, scripts, Git history, prompt files, or generated metadata.

The skill must use the official DashScope API path and must not require browser automation, Gemini cookies, Docker containers, or host-browser control for video generation.

## Media pipeline

The runtime pipeline is:

    image_gen still frame
            ↓
    local Python
            ↓
    DashScope SDK
            ↓
    Alibaba Cloud Bailian
            ↓
    wan3.0-video
            ↓
    generated MP4 downloaded locally
            ↓
    FFmpeg captioning / audio mixing / stitching / QA

Preserve the model-generated ambience unless the user explicitly requests otherwise.
