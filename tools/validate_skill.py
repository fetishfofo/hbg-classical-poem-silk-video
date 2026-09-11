#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "classical-poem-silk-video"


def main() -> int:
    errors: list[str] = []
    skill_md = SKILL / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append("SKILL.md has no valid YAML frontmatter block")
    else:
        lines = [line for line in match.group(1).splitlines() if line.strip()]
        keys = [line.split(":", 1)[0].strip() for line in lines if ":" in line]
        if keys != ["name", "description"]:
            errors.append(f"frontmatter keys must be name, description; got {keys}")
        if "name: classical-poem-silk-video" not in match.group(1):
            errors.append("skill name mismatch")

    required = [
        "agents/openai.yaml",
        "references/runtime-contract.md",
        "references/style-and-scene-mapping.md",
        "scripts/check_wan3_prerequisites.sh",
        "scripts/wan3_i2v.sh",
        "scripts/wan3_i2v.py",
        "scripts/make_scene_ass.py",
        "scripts/render_scene.sh",
        "scripts/concat_poem_crossfade.sh",
        "scripts/final_media_qa.sh",
        "assets/MaShanZheng-Regular.ttf",
        "assets/OFL.txt",
    ]
    for relative in required:
        if not (SKILL / relative).is_file():
            errors.append(f"missing {relative}")

    if (SKILL / "README.md").exists():
        errors.append("README.md must stay outside the skill folder")
    if list(SKILL.rglob("__pycache__")) or list(SKILL.rglob("*.pyc")):
        errors.append("Python cache files must not be committed")

    yaml_text = (SKILL / "agents/openai.yaml").read_text(encoding="utf-8")
    if "$classical-poem-silk-video" not in yaml_text:
        errors.append("agents/openai.yaml default_prompt must mention $classical-poem-silk-video")

    for target in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)", text):
        if "://" in target or target.startswith("#"):
            continue
        if not (SKILL / target).exists():
            errors.append(f"broken SKILL.md link: {target}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print("Skill structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
