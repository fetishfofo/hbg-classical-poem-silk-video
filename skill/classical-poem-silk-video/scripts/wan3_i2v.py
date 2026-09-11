#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import mimetypes
import os
import urllib.request
from http import HTTPStatus
from pathlib import Path

import dashscope
from dashscope import VideoSynthesis


def image_to_data_uri(path: Path) -> str:
    """把本地图片转换成 Wan 3.0 可以接收的 Base64 Data URI。"""
    if not path.is_file():
        raise FileNotFoundError(f"Input image not found: {path}")

    mime_type, _ = mimetypes.guess_type(path.name)
    if mime_type not in {
        "image/jpeg",
        "image/png",
        "image/webp",
        "image/bmp",
    }:
        raise ValueError(f"Unsupported image type: {mime_type}")

    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def main() -> int:
    # 保持与原 Gemini I2V 相同的三个核心输入接口
    image = Path(os.environ["POEM_I2V_IMAGE"])
    output = Path(os.environ["POEM_I2V_OUTPUT"])
    prompt = os.environ["POEM_I2V_PROMPT"]

    # 百炼配置
    api_key = os.environ["DASHSCOPE_API_KEY"]
    dashscope.base_http_api_url = os.environ["DASHSCOPE_BASE_URL"]

    # 可选参数；不设置时使用这些默认值
    resolution = os.environ.get("POEM_I2V_RESOLUTION", "720P")
    duration = int(os.environ.get("POEM_I2V_DURATION", "5"))
    ratio = os.environ.get("POEM_I2V_RATIO", "adaptive")

    output.mkdir(parents=True, exist_ok=True)

    print(f"Input image: {image}")
    print("Encoding local image...")
    image_data_uri = image_to_data_uri(image)

    print("Calling Wan 3.0...")

    rsp = VideoSynthesis.call(
        api_key=api_key,
        model="wan3.0-video",
        prompt=prompt,
        media=[
            {
                "type": "first_frame",
                "url": image_data_uri,
            }
        ],
        resolution=resolution,
        ratio=ratio,
        duration=duration,
    )

    if rsp.status_code != HTTPStatus.OK:
        raise RuntimeError(
            f"Wan 3.0 generation failed: "
            f"status_code={rsp.status_code}, "
            f"code={rsp.code}, "
            f"message={rsp.message}"
        )

    video_url = rsp.output.video_url
    video_path = output / "poem-scene-1.mp4"

    print("Generation complete.")
    print("Downloading video...")
    urllib.request.urlretrieve(video_url, video_path)

    result = {
        "status": "complete",
        "provider": "dashscope",
        "model": "wan3.0-video",
        "video_count": 1,
        "saved": [
            {
                "path": str(video_path),
                "filename": video_path.name,
            }
        ],
        "resolution": resolution,
        "duration": duration,
        "ratio": ratio,
    }

    (output / "result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Saved video: {video_path}")
    print(json.dumps(result["saved"], ensure_ascii=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
