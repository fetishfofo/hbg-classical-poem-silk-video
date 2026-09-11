<p align="center">
  <img src="docs/showcase/hero.svg" alt="HBG Classical Poem Silk Video" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/Mr-funny/hbg-classical-poem-silk-video/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/Mr-funny/hbg-classical-poem-silk-video/ci.yml?branch=main&style=flat-square&label=CI" alt="CI" /></a>
  <img src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-8b5cf6?style=flat-square" alt="Agent Skill" />
  <img src="https://img.shields.io/badge/Canvas-1080%C3%971920-b45309?style=flat-square" alt="1080x1920" />
  <img src="https://img.shields.io/badge/Stills-ImageGen-2563eb?style=flat-square" alt="ImageGen" />
  <img src="https://img.shields.io/badge/I2V-Wan%203.0-0f766e?style=flat-square" alt="Wan 3.0 I2V" />
  <img src="https://img.shields.io/badge/Audio-ambience%20%2B%20BGM-c2410c?style=flat-square" alt="Ambience and BGM" />
  <img src="https://img.shields.io/badge/QA-final%20MP4-25221f?style=flat-square" alt="Final MP4 QA" />
</p>

<p align="center">
  把古诗词做成<strong>逐句或两句一景的竖屏中国画动态视频</strong>。<br />
  <strong>诗意分镜 · 中国画风格分化 · 画中物象真实运动 · 毛笔字逐字题写 · 原环境声与 BGM 并行 · 最终成片质检</strong>
</p>

> 这不是“给一张古画做慢速推镜”的模板。Skill 会把诗句拆成独立意象，用静态锚点限制图生视频重画，让水纹、飞鸟、马蹄、柳枝、衣袍等画中物象真正动起来。

## ⚡ 一句话安装进 Agent

把下面整段话发给 Codex、Claude Code 或其他支持 `SKILL.md` 的 Agent：

```text
请从 https://github.com/Mr-funny/hbg-classical-poem-silk-video 安装
classical-poem-silk-video skill。

请自动识别当前 Agent 的全局 skills 目录；如果已经存在旧版本，请先备份再更新。
安装后检查 SKILL.md、agents、references、scripts 和字体资产是否完整，
运行 shell 语法检查、Python 编译检查与 skill 校验。
不要读取、打印或上传任何 API Key、Cookie、Chrome Profile、本地视频、音频或生成素材。

验证完成后，告诉我如何使用 $classical-poem-silk-video
把一首中国古诗制作成 1080×1920 的国风动态视频。
```

安装后直接说：

```text
使用 $classical-poem-silk-video 制作《枫桥夜泊》。
四句诗一行一景，画面色调跟随诗意变化；镜头固定，
让月光、水纹、乌鸦、霜雾和渔火在画中自然运动。
保留 AI 环境原声，毛笔字逐字出现，场景之间自然交叉溶解。
```

## 🎯 它解决的不是“古画会动”，而是“古画不会乱动”

| 常见问题 | Skill 的处理方式 |
|---|---|
| 每张图都是同一种泛黄古绢色 | 保持中国画 DNA，一景一条风格通道：水墨、工笔、青绿、人物鞍马等 |
| 用后期推镜冒充图生动态 | 默认锁定镜头，只允许已有物象做局部、可解释的动作 |
| 云雾一动就变成祥云，寺庙被重新搭建 | 声明建筑、山体、树干、岸线、人物躯干为静态锚点 |
| 鸟越动越多，枝条凭空生长 | 固定主体数量与身体中心，明确禁止复制、合并、长枝和新增剪影 |
| 马匹走动时多腿、悬空或换身体 | 限制为一次重心变化或小步，检查四蹄、地面接触和身体一致性 |
| 所有动作同时发生导致整幅画重构 | 每景只设一个主动作，加一到两个环境辅助动作 |
| 转场时黑一下，环境声突然断掉 | 画面用 `xfade`，原环境声用 `acrossfade`，BGM 连续播放 |
| 图生视频阶段依赖浏览器自动化或海外服务 | 使用阿里云百炼 Wan 3.0 官方 DashScope API，直接从本地首帧生成视频 |
| 字幕像普通视频字体 | 内置 Ma Shan Zheng，右列先写、左列后写，逐字出现 |
| 浏览器预览没问题，最终 MP4 却有黑帧 | 对最终编码视频重新抽帧、检查转场中点、末帧、黑帧和音轨 |

## ✨ 核心能力

| 模块 | 能力 |
|---|---|
| 诗词解析 | 识别时代、地点、季节、时间、意象、动作和情绪弧线 |
| 分镜分组 | 四句以内默认逐句；长诗默认连续两句一景 |
| 画面风格 | 在统一中国画品质下，按诗意切换水墨、工笔、青绿、鞍马等支线 |
| 静帧生成 | 使用 Codex 内置 ImageGen，预留竖排题字安全区 |
| 图生视频 | 通过 DashScope 调用阿里云百炼 Wan 3.0，以本地静帧作为首帧生成视频 |
| 动作提示词 | 静态锚点、局部动作区、稳定收尾、反幻觉禁令四段式结构 |
| 字幕 | Ma Shan Zheng 毛笔字体，两列竖排，按字揭示 |
| 音频 | 保留每个 I2V 镜头的模型环境声，可叠加连续 BGM |
| 转场 | 画面和环境声同步交叉溶解，避免黑场与音频重启 |
| QA | 检查主体数量、动物肢体、建筑稳定、题字安全区、编码规格与末帧 |

## 🚀 快速开始

### 方法一：让 Agent 自动安装（推荐）

复制 README 首屏的自然语言安装提示，让 Agent 完成下载、备份、安装和验证。

### 方法二：安装到 Codex

```bash
curl -fsSL https://raw.githubusercontent.com/Mr-funny/hbg-classical-poem-silk-video/main/install.sh | sh
```

默认安装到：

```text
${CODEX_HOME:-~/.codex}/skills/classical-poem-silk-video
```

### 方法三：安装到 Claude Code

```bash
curl -fsSL https://raw.githubusercontent.com/Mr-funny/hbg-classical-poem-silk-video/main/install.sh | sh -s -- --claude
```

### 方法四：手动安装

```bash
git clone https://github.com/Mr-funny/hbg-classical-poem-silk-video.git
mkdir -p ~/.codex/skills/classical-poem-silk-video
cp -R hbg-classical-poem-silk-video/skill/classical-poem-silk-video/. \
  ~/.codex/skills/classical-poem-silk-video/
```

## ☁️ Wan 3.0 运行时

静帧由 Agent 的内置 ImageGen 生成。图生视频使用阿里云百炼 Wan 3.0，并通过官方 DashScope API 调用。

运行环境需要：

- Python 3
- DashScope Python SDK
- FFmpeg 和 ffprobe
- ripgrep
- 已开通阿里云百炼 `wan3.0-video`
- `DASHSCOPE_API_KEY`
- `DASHSCOPE_BASE_URL`

建议在项目的 Python 虚拟环境中安装 DashScope：

    pip install -U dashscope

在当前终端会话中设置百炼环境变量：

    export DASHSCOPE_API_KEY="YOUR_API_KEY"
    export DASHSCOPE_BASE_URL="YOUR_DASHSCOPE_NATIVE_API_BASE_URL"

不要把真实 API Key 写入 README、脚本、Git 提交或其他项目文件。

配置完成后运行：

    skill/classical-poem-silk-video/scripts/check_wan3_prerequisites.sh

图生视频调用链：

    scripts/wan3_i2v.sh
        ↓
    scripts/wan3_i2v.py
        ↓
    DashScope
        ↓
    Alibaba Cloud Bailian
        ↓
    wan3.0-video

本地静帧会作为 `first_frame` 输入发送给 Wan 3.0，生成的视频自动下载到项目的 `outputs/wan3/`。

正常的首帧图生视频不依赖 Docker、Gemini Cookie、浏览器自动化或 HBG Gemini Flow Suite。

详细运行约定见 [runtime-contract.md](skill/classical-poem-silk-video/references/runtime-contract.md)。

## 🤖 使用示例

### 四句逐句成画

```text
使用 $classical-poem-silk-video 制作《枫桥夜泊》。
每句一景，夜色从冷蓝过渡到渔火暖色。
不要做后期推镜，动态来自月光、水纹、乌鸦、霜雾和钟声的可见原因。
```

### 长诗两句一景

```text
使用 $classical-poem-silk-video 制作《钱塘湖春行》。
两句一景，共四景；水墨湖寺、工笔花鸟、人物鞍马、青绿长堤分别对应诗意。
保留 AI 原环境声，BGM 与原声并行，转场使用 1.2 秒自然溶解。
```

### 修复已有国风视频

```text
使用 $classical-poem-silk-video 检查这四段图生视频。
重点排查建筑重构、鸟类复制、马腿畸形、柳叶脱落、字幕安全区和黑帧转场。
只重做不合格镜头，不要用后期推镜掩盖问题。
```

## 🧠 工作原理

```mermaid
flowchart LR
    A["完整古诗词"] --> B["意象与情绪弧线"]
    B --> C["逐句 / 两句一景"]
    C --> D["中国画风格通道"]
    D --> E["ImageGen 静帧"]
    E --> F["Wan 3.0 I2V"]
    F --> G["早中晚抽帧验收"]
    G --> H["毛笔字逐字字幕"]
    H --> I["原环境声 + BGM"]
    I --> J["画面与声音交叉溶解"]
    J --> K["最终 MP4 QA"]
```

四条动作原则：

1. **镜头锁定。** 图生视频的动态来自画中物象，不来自后期缩放。
2. **动作有锚点。** 翅膀围绕身体中心，水纹从接触点扩散，柳叶不能离开枝条。
3. **一景一主动作。** 动作过多会诱发模型重新构图。
4. **最终 MP4 才是交付对象。** 必须从编码后的成片重新抽帧验收。

## 🖼️ 实际项目：钱塘湖春行

<p align="center">
  <img src="docs/showcase/qian-tang-contact.jpg" alt="钱塘湖春行关键帧" width="72%" />
</p>

- 8 句诗，连续两句一景，共 4 景
- 水墨湖寺、工笔花鸟、人物鞍马、青绿长堤四条视觉通道
- 每景约 9 秒，3 次 1.2 秒交叉溶解
- 最终规格：1080×1920、30fps、H.264 + AAC
- 成片时长：32.44 秒
- 保留 I2V 原环境声，支持 BGM 低铺底或 100% 并行混音

[下载示例成片（GitHub Release）](https://github.com/Mr-funny/hbg-classical-poem-silk-video/releases/download/v0.1.0/qian-tang-hu-chun-xing-v4-full-bgm.mp4)

完整复盘文章：

> [《我用 Codex + AI 生图 + Wan 3.0，把〈钱塘湖春行〉做成了一条会呼吸的中国画视频》](docs/article.md)

## ✅ 最终媒体质检

```bash
skill/classical-poem-silk-video/scripts/final_media_qa.sh \
  final.mp4 qa/final
```

输出包括：

- `ffprobe.json`
- `blackdetect.log`
- `silencedetect.log`
- `volumedetect.log`
- 10%、25%、50%、75%、90% 与末帧
- 最终编码视频联系表

如需检查马蹄、鸟数或转场中点，准备 TSV：

```text
8.400\ttransition-1-mid
16.200\ttransition-2-mid
20.100\thorse-contact
24.000\ttransition-3-mid
```

```bash
skill/classical-poem-silk-video/scripts/final_media_qa.sh \
  final.mp4 qa/final qa-timestamps.tsv
```

## 📁 仓库结构

```text
skill/classical-poem-silk-video/  Agent Skill 本体
docs/article.md                   当前项目完整复盘文章
docs/showcase/                    README 视觉预览
examples/                         脱敏示例分镜与提示词
tools/                            CI 校验与隐私扫描
install.sh                        Codex / Claude Code 安装器
```

## 🔐 隐私与合规

- 不提交 API Key、Cookie、`.env`、Chrome Profile、Docker 数据卷或生成账号数据。
- 不提交用户原始聊天、私人文案、本地项目路径或未授权素材。
- 只在用户要求且适用条款允许时处理白色模型星标；传统红印与有意画面标记必须保留。
- 运行时凭据由用户本人配置，Skill 的视频生成流程只通过 DashScope API 调用阿里云百炼 Wan 3.0。

## 📄 License

- Skill、脚本与文档：MIT License
- Ma Shan Zheng 字体：SIL Open Font License 1.1，见 `skill/classical-poem-silk-video/assets/OFL.txt`
- 阿里云百炼 Wan 3.0：通过官方 DashScope API 调用，本仓库不包含或分发模型服务本身

欢迎提交 Issue 和 PR，一起把“这次终于改对了”变成“下一次默认不会再错”。
