# w-slide-lecturer

**PPT 逐模块英文授课讲稿 Skill（v2.0）**

给正在进行英文技术课程授课的讲师使用。把一个 PPTX / PDF 变成：

- 每页按**原始视觉模块**的 A 原文（修复异常换行） → B 英文授课稿 → C 中文指图提示；
- 讲稿详细、顺着原文读，尽量直接复用 PPT 原句；
- 独立 Markdown 和含所有原页截图的 ZIP。

## 安装

将完整 `w-slide-lecturer/` 目录放到你的 Agent 支持的 Skills 搜索路径：

```text
macOS / Linux: ~/.agents/skills/w-slide-lecturer/SKILL.md
Windows: %USERPROFILE%\.agents\skills\w-slide-lecturer\SKILL.md
```

支持的 Codex 环境通常会扫描此路径；如产品有自己的 Skill 路径，以其当前文档为准。**放置目录后重新启动会话 / 刷新 Skills**。这份 ZIP 是本地可安装的 Skill 包，**不会自动上传或安装进你的账户**。

## 调用示例

```
使用 $w-slide-lecturer，为附件《课程.pptx》生成完整英文授课 Markdown 讲稿。
按每一页 PPT 的视觉模块顺序组织：每个模块给出修正断行的 PPT 原文、
优先用原句写的详细英文讲稿和中文指图提示。禁止跨模块跳转。
讲完当前页后再写到下一页的 Transition。
最后提供 Markdown 和含每页原图的 ZIP。
```

## 文件结构

```text
w-slide-lecturer/
├── SKILL.md                 # 核心行为与执行规则
├── README.md                # 安装与调用
├── scripts/
│   ├── prepare_slides.py    # PPTX/PDF 可编辑文本提取、位置记录、可选渲染
│   └── validate_output.py   # 讲稿结构检查（不代替逐页目视审校）
├── references/
│   ├── extraction.md        # 原文、图片、断行修复规范
│   ├── speaking.md          # 模块式英文讲解规则与示例
│   └── quality.md           # 完整性与质量审校
└── assets/
    └── module-template.md   # Markdown 模板
```

## 环境要求

- 提取 PPTX 文字：`pip install python-pptx`；提取 PDF 文字/图片：`pip install pymupdf`
- PPTX 转图片（可选）：安装 `LibreOffice`，需能运行 `libreoffice` 或 `soffice`
- 图片烘焙文字仍须由**具备视觉读取能力的模型或人工**核对；脚本不承诺 OCR 全量识别

```bash
python scripts/prepare_slides.py "/path/course.pptx" --out "/path/work" --render
python scripts/validate_output.py "/path/work/final.md" --manifest "/path/work/source_manifest.json" --images-root "/path/work"
```

脚本生成 `selectable_text.md` / JSON / 截图，**不是自动生成最终英文讲解**；仍需 Agent 严格完成视觉分组、原文核对、英文授课稿撰写。

## 和旧版 ppt-lecture-script 的区别

1. A、B、C 不再拆成三个整页区，而是**每个模块就地排列 A → B → C**。
2. 每个模块必须先讲完，**禁止不同区域交叉穿插**。
3. 原文直接用于英文讲稿，**少改写、少扩写，确保讲师能对照原页讲**。
4. 清理转换带来的断句/换行，但保持原词、公式、表格与真实段落。

参照格式：[Agent Skills 标准](https://agentskills.io/specification)。
