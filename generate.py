"""
Hermes Skin Gallery — YAML Generator

Parses the preview/index.html file and extracts all 67 skin definitions,
then generates individual .yaml files in the skins/ directory.

Usage:
    python generate.py

Requirements:
    Python 3.7+ (stdlib only, no external deps)
"""

import re
import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
HTML_PATH = BASE_DIR / 'preview' / 'index.html'
SKINS_DIR = BASE_DIR / 'skins'


def parse_colors(text: str) -> dict:
    """Parse colors block like: key: '#value', ..."""
    pairs = re.findall(r"(\w+):\s*'(#[^']+)'", text)
    return {k: v for k, v in pairs}


def parse_spinner(text: str) -> dict:
    """Parse spinner block: { waiting: ['a','b'], verbs: ['c','d'] }"""
    waiting_match = re.search(r"waiting:\s*\[([^\]]+)\]", text)
    verbs_match = re.search(r"verbs:\s*\[([^\]]+)\]", text)
    waiting = re.findall(r"'([^']*)'", waiting_match.group(1)) if waiting_match else []
    verbs = re.findall(r"'([^']*)'", verbs_match.group(1)) if verbs_match else []
    return {'waiting': waiting, 'verbs': verbs}


def parse_branding(text: str) -> dict:
    """Parse branding block: { agent: 'x', welcome: 'x', prompt: 'x', label: 'x' }"""
    return {
        'agent': (m.group(1) if (m := re.search(r"agent:\s*'([^']*)'", text)) else ''),
        'welcome': (m.group(1) if (m := re.search(r"welcome:\s*'([^']*)'", text)) else ''),
        'prompt': (m.group(1) if (m := re.search(r"prompt:\s*'([^']*)'", text)) else ''),
        'label': (m.group(1) if (m := re.search(r"label:\s*'([^']*)'", text)) else ''),
    }


def gen_yaml(skin: dict) -> str:
    """Generate a complete Hermes skin YAML from a skin dict."""
    c = skin['colors']
    sp = skin['spinner']
    b = skin['branding']

    lines = [
        f'name: {skin["id"]}',
        f'description: "{skin["cat"]} — {skin["desc"]}"',
        f'mode: {skin["mode"]}',
        'colors:',
    ]
    color_keys = [
        'banner_border', 'banner_title', 'banner_accent', 'banner_dim',
        'banner_text', 'ui_accent', 'ui_label', 'ui_ok', 'ui_error',
        'ui_warn', 'prompt', 'input_rule', 'response_border',
        'status_bar_bg', 'session_label', 'session_border',
    ]
    for key in color_keys:
        lines.append(f'  {key}: "{c.get(key, "")}"')

    lines.append('spinner:')
    lines.append('  waiting_faces:')
    for f in sp['waiting']:
        lines.append(f'    - "{f}"')
    lines.append('  thinking_verbs:')
    for v in sp['verbs']:
        lines.append(f'    - "{v}"')

    lines.append('branding:')
    lines.append(f'  agent_name: "{b["agent"]}"')
    lines.append(f'  welcome: "{b["welcome"]}"')
    lines.append(f'  prompt_symbol: "{b["prompt"]}"')
    lines.append(f'  response_label: "{b["label"]}"')
    lines.append('tool_prefix: "┊"')
    lines.append('')

    return '\n'.join(lines)


def main():
    if not HTML_PATH.exists():
        print(f"ERROR: {HTML_PATH} not found. Run from project root.")
        return

    html = HTML_PATH.read_text(encoding='utf-8')

    # Extract SKINS array
    match = re.search(r'const SKINS = \[(.*?)\n\];', html, re.DOTALL)
    if not match:
        print("ERROR: Could not find SKINS array in HTML")
        return

    skins_text = match.group(1)

    # Parse all skin objects
    skin_objects = re.findall(
        r"id:\s*'(\S+)',\s*name:\s*'([^']+)',\s*mode:\s*'(dark|light)',\s*"
        r"\n\s*cat:\s*'([^']+)',\s*desc:\s*'([^']+)',\s*"
        r"\n\s*bg:\s*'(#[^']+)',\s*fg:\s*'(#[^']+)',\s*"
        r"\n\s*colors:\s*\{(.*?)\},\s*"
        r"\n\s*spinner:\s*\{(.*?)\},\s*"
        r"\n\s*branding:\s*\{(.*?)\}",
        skins_text, re.DOTALL
    )

    if not skin_objects:
        print("ERROR: Could not parse any skins")
        return

    print(f"Found {len(skin_objects)} skins")

    # Ensure output directory
    SKINS_DIR.mkdir(parents=True, exist_ok=True)

    dark_count = light_count = 0
    summary_skins = []

    for s in skin_objects:
        sid, name, mode, cat, desc, bg, fg, colors_text, spinner_text, branding_text = s
        skin = {
            'id': sid, 'name': name, 'mode': mode,
            'cat': cat, 'desc': desc, 'bg': bg, 'fg': fg,
            'colors': parse_colors(colors_text),
            'spinner': parse_spinner(spinner_text),
            'branding': parse_branding(branding_text),
        }

        yaml_content = gen_yaml(skin)
        (SKINS_DIR / f'{sid}.yaml').write_text(yaml_content, encoding='utf-8')

        if mode == 'dark':
            dark_count += 1
        else:
            light_count += 1

        summary_skins.append({'id': sid, 'name': name, 'mode': mode, 'cat': cat, 'desc': desc})

    # Write summary JSON
    summary = {
        'total': len(skin_objects),
        'dark': dark_count,
        'light': light_count,
        'skins': summary_skins,
    }
    (BASE_DIR / 'skins.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )

    print(f"Done! {dark_count} dark + {light_count} light = {len(skin_objects)} YAML files")
    print(f"Output: {SKINS_DIR}/")


if __name__ == '__main__':
    main()
