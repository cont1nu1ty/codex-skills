# Codex Skills

个人常用的 Codex skill 合集，按 `skills/<skill-name>/` 独立维护，后续可以继续添加其他技能。

GitHub 仓库：[cont1nu1ty/codex-skills](https://github.com/cont1nu1ty/codex-skills)。

## 技能目录

| Skill | 用途 |
| --- | --- |
| [critical-blog-reader](skills/critical-blog-reader/SKILL.md) | 批判性阅读博客与文章，展开作者逻辑、整理 Hacker News 分歧，综合形成有证据、有边界的结论 |

`critical-blog-reader` 默认使用中等详细度的中文，按原文长度调整篇幅。它使用宿主已有的网页搜索和读取能力，无需单独 API 密钥或 MCP 服务；无法访问或尚未核实的内容会明确说明。详细度参考见 [calibration.md](skills/critical-blog-reader/references/calibration.md)。

## 安装与使用

在另一台电脑的 Codex 中发送：

> 使用 $skill-installer 从 https://github.com/cont1nu1ty/codex-skills 的 skills/critical-blog-reader 目录安装技能。

也可以将 `skills/critical-blog-reader` 文件夹交给 Codex，要求安装到本机个人技能目录。安装器支持从其他 GitHub 仓库下载技能；如果新技能没有出现，可重启 Codex。见 [官方技能说明](https://learn.chatgpt.com/docs/build-skills)。

安装后使用：

> 使用 $critical-blog-reader 阅读这篇文章：[文章链接]。如有对应 Hacker News 讨论，也一起分析。

> 使用 $critical-blog-reader 分析以下两篇文章，展开作者逻辑、HN 不同意见与热门争论，最后综合判断：[文章链接]。

本地安装不会自动与 GitHub 持续同步。仓库更新后，再更新本机技能；更新前比较并保留本地修改。

## 添加其他技能

1. 在 `skills/` 下新建以技能名称命名的目录。
2. 添加 `SKILL.md`，在 YAML frontmatter 中填写 `name` 和 `description`；按实际需要增加 `agents/`、`references/`、`scripts/` 或 `assets/`。
3. 更新上面的技能目录，检查相对链接，并验证新增技能的结构与实际行为。
4. 如需重新打包整个合集，更新 `plugin.json` 的版本、当前能力描述及发布说明。

## 可选：插件打包

仓库保留随附件提供的插件元数据与图标。根目录 `plugin.json` 使用 portable Agent Plugins 格式，`skills/` 下的技能会由该格式自动发现。见 [官方打包说明](https://developers.openai.com/plugins/build/plugins)。

打包器仅依赖 Python 3.9 或更新版本的标准库。从本目录运行：

```bash
python3 tools/package_plugin.py dist/codex-skills-plugin.zip
```

打包只包含 `plugin.json`、`assets/` 和 `skills/`；`dist/` 已忽略。输出必须是 `.zip` 文件，并放在 `assets/`、`skills/` 之外。打包器会拒绝源文件符号链接，避免意外纳入目录外内容。

GitHub 上传与官方插件目录提交是两个独立操作。本仓库尚未提交官方审核或在官方插件目录发布。可选提交流程及验证边界见 [SUBMISSION.md](SUBMISSION.md)。

## 文件结构

```text
codex-skills/
├── README.md
├── SUBMISSION.md
├── plugin.json
├── assets/icon.png
├── skills/
│   └── critical-blog-reader/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/calibration.md
└── tools/package_plugin.py
```
