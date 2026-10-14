#!/usr/bin/env python3
"""Validate slide/module structure of a completed w-slide-lecturer Markdown file.

Important: This cannot check truthfulness of source words or visual reading order.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
import sys
from pathlib import Path

SLIDE = re.compile(r"(?m)^## Slide\s+(\d+)\s*[—\-]\s*\S.*$")
MODULE = re.compile(r"(?m)^### Module\s+(\d+)\s*[—\-]\s*\S.*$")
A = re.compile(r"(?m)^#### A\.\s*PPT(?:\s+原文|\s+Original Text)")
B = re.compile(r"(?m)^#### B\.\s*English Teaching Script")
C = re.compile(r"(?m)^#### C\.\s*中文授课提示")
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
TRANSITION = re.compile(r"\*\*Transition to (?:Next Slide|Slide \d+)[^\n]*\*\*")
FILLER = re.compile(r"\{(?:该模块|模块\s*\d|下一页|指图|原始|课程名)|\[(?:TODO|待填写|待补|PLACEHOLDER)", re.IGNORECASE)


def check(md_file: Path, manifest_file: Path, image_root: Path) -> int:
    data = md_file.read_text(encoding="utf-8")
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    expected = manifest["slide_count"]
    matches = list(SLIDE.finditer(data))
    indices = [int(m.group(1)) for m in matches]
    errors, warnings = [], []
    if indices != list(range(1, expected + 1)):
        errors.append(f"Slide numbers {indices} differ from expected 1..{expected}")
    total_modules = 0
    c_bodies = []
    for idx, match in enumerate(matches):
        num = int(match.group(1))
        tail = matches[idx + 1].start() if idx + 1 < len(matches) else len(data)
        chunk = data[match.end():tail]
        img = f"slide_images/slide_{num:02d}.png"
        if img not in IMAGE.findall(chunk):
            errors.append(f"Slide {num:02d}: missing screenshot reference {img}")
        elif not (image_root / img).is_file():
            errors.append(f"Slide {num:02d}: screenshot not found at {image_root / img}")
        modules = list(MODULE.finditer(chunk))
        if not modules:
            errors.append(f"Slide {num:02d}: no visual modules")
            continue
        mod_nums = [int(m.group(1)) for m in modules]
        if mod_nums != list(range(1, len(modules) + 1)):
            errors.append(f"Slide {num:02d}: module numbers should be 1..{len(modules)}, got {mod_nums}")
        total_modules += len(modules)
        for mi, mod in enumerate(modules):
            mend = modules[mi + 1].start() if mi + 1 < len(modules) else len(chunk)
            body = chunk[mod.end():mend]
            marks = [A.search(body), B.search(body), C.search(body)]
            if not all(marks):
                errors.append(f"Slide {num:02d}, module {mi+1:02d}: expected A/B/C subsections")
                continue
            if not (marks[0].start() < marks[1].start() < marks[2].start()):
                errors.append(f"Slide {num:02d}, module {mi+1:02d}: incorrect A→B→C order")
            else:
                original = body[marks[0].end():marks[1].start()].strip()
                spoken = body[marks[1].end():marks[2].start()].split("\n", 1)[-1].strip()
                cues = body[marks[2].end():].split("\n", 1)[-1].split("**Transition to", 1)[0].strip()
                if not original or not spoken:
                    errors.append(f"Slide {num:02d}, module {mi+1:02d}: empty original/script")
                if re.search(r"[\u4e00-\u9fff]", spoken):
                    warnings.append(f"Slide {num:02d}, module {mi+1:02d}: Chinese found in spoken English; move cues to C")
                if cues:
                    c_bodies.append(re.sub(r"\s+", " ", cues))
        if num < expected:
            tr = TRANSITION.search(chunk)
            if tr is None:
                warnings.append(f"Slide {num:02d}: no explicit next-slide transition marker")
            elif tr.start() < modules[-1].end():
                errors.append(f"Slide {num:02d}: transition appears before last module")
        if FILLER.search(chunk):
            errors.append(f"Slide {num:02d}: template placeholder remains")
    repeats = Counter(c_bodies).most_common(1)
    if repeats and repeats[0][1] >= max(8, len(c_bodies) // 5):
        warnings.append(f"Highly repetitive Chinese pointing cues: identical C text used in {repeats[0][1]} modules; review actual locations")
    print(f"Source slides: {expected}; Markdown slides: {len(matches)}; Modules: {total_modules}")
    for msg in errors:
        print("ERROR:", msg)
    for msg in warnings:
        print("WARN:", msg)
    print(f"Structure: {len(errors)} error(s), {len(warnings)} warning(s)")
    print("Reminder: visual module order, source fidelity, and spoken-script quality require manual review.")
    return 1 if errors else 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("markdown", type=Path)
    p.add_argument("--manifest", required=True, type=Path)
    p.add_argument("--images-root", type=Path, default=None)
    opt = p.parse_args()
    return check(opt.markdown, opt.manifest, opt.images_root or opt.markdown.parent)


if __name__ == "__main__":
    sys.exit(main())
