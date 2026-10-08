# 官方插件目录提交说明

## 状态

本仓库用于在 GitHub 维护和分发个人技能合集。官方插件目录尚未上传、提交审核或发布；GitHub 仓库可访问不代表官方审核通过。

插件元数据沿用附件中的发布者署名 `continuity`。尚未核验平台中的发布身份；提交前确认 `extensions.com.openai.interface.developerName` 与 `author.name` 符合实际身份。如有改动，重新打包。

## 可选提交流程

1. 检查所有技能、参考文件及图标，确认待公开的内容。
2. 从仓库根目录运行 `python3 tools/package_plugin.py dist/codex-skills-plugin.zip`。
3. 按 [官方上传与提交说明](https://developers.openai.com/plugins/deploy/submission)，在 [OpenAI 平台插件页面](https://platform.openai.com/plugins) 选择所属组织、项目和已验证发布身份，上传 ZIP。
4. 检查平台自动校验结果，必要时修正源码并重新打包上传；完成平台要求后提交审核。
5. 审核通过后再选择发布。上传、提交审核、公开发布是不同状态。

当前合集只有技能，没有 MCP 服务。官方说明允许 skills-only 插件省略 MCP 审核案例与演示视频；最终要求以平台检查结果为准。打包结构见 [官方打包说明](https://developers.openai.com/plugins/build/plugins)。

## 验证边界

本地可检查技能 frontmatter、名称、引用文件、插件资源路径及 ZIP CRC。这些检查不能替代平台元数据校验、官方审核或真实阅读任务的行为评测。

附件中的详细度校准资料保留为风格参考；本次整理没有重新执行其中两篇文章的阅读评测，也没有核验历史认可记录。
