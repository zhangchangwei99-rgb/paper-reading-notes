"""Validate this skill's portable, dependency-free package conventions."""
from pathlib import Path
import json
import re
import sys


def validate(root):
    errors = []
    required = [
        'SKILL.md', 'README.md', 'LICENSE', 'CHANGELOG.md', 'agents/openai.yaml',
        'references/style-evidence.md', 'references/reading-protocol.md',
        'references/note-template.md', 'references/publishing.md',
        'references/quality-gates.md',
    ]
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f'Missing file: {relative}')
    texts = {}
    for path in root.rglob('*'):
        if path.is_file() and path.suffix in {'.md', '.yaml', '.py'}:
            try:
                text = path.read_text(encoding='utf-8')
                texts[path] = text
            except UnicodeError:
                errors.append(f'Invalid UTF-8: {path.relative_to(root)}')
                continue
            if '\ufffd' in text or text.startswith('\ufeff'):
                errors.append(f'Encoding artifact: {path.relative_to(root)}')
            if path.suffix in {'.md', '.yaml'}:
                if re.search(r'(?<!\w)[A-Za-z]:[\\/]', text):
                    errors.append(f'Local Windows path: {path.relative_to(root)}')
                if re.search(r'/(?:Users|home)/[A-Za-z0-9_.-]+/', text):
                    errors.append(f'Personal absolute path: {path.relative_to(root)}')
            if path.suffix == '.md':
                for link in re.findall(r'\]\(([^)]+)\)', text):
                    if '://' in link or link.startswith('#'):
                        continue
                    target = (path.parent / link.split('#', 1)[0]).resolve()
                    if not target.is_relative_to(root) or not target.is_file():
                        errors.append(f'Invalid reference: {path.relative_to(root)} -> {link}')

    skill = texts.get(root / 'SKILL.md', '')
    front = re.match(r'\A---\n(.*?)\n---(?:\n|$)', skill, re.S)
    if not front:
        errors.append('Invalid frontmatter delimiters')
    else:
        fields = {}
        for line in front.group(1).splitlines():
            key, separator, value = line.partition(':')
            if not separator or not value.strip():
                errors.append(f'Invalid simple frontmatter field: {line}')
                continue
            if key in fields:
                errors.append(f'Duplicate frontmatter key: {key}')
            fields[key] = value.strip()
        if fields.get('name') != 'paper-reading-notes':
            errors.append('Unexpected skill name')
        if not 1 <= len(fields.get('description', '')) <= 1024:
            errors.append('Invalid skill description length')
        if set(fields) != {'name', 'description'}:
            errors.append('Unexpected simple frontmatter schema')

    ui = texts.get(root / 'agents' / 'openai.yaml', '')
    ui_fields = {}
    for key in ['display_name', 'short_description', 'default_prompt']:
        match = re.search(r'^  ' + key + r': (.+)$', ui, re.M)
        try:
            value = json.loads(match.group(1)) if match else None
        except json.JSONDecodeError:
            value = None
        if not isinstance(value, str) or not value:
            errors.append(f'Invalid quoted interface field: {key}')
        else:
            ui_fields[key] = value
    if not 25 <= len(ui_fields.get('short_description', '')) <= 64:
        errors.append('Invalid interface description length')
    if '$paper-reading-notes' not in ui_fields.get('default_prompt', ''):
        errors.append('Default prompt must invoke the skill')
    return errors


if __name__ == '__main__':
    package_root = Path(__file__).resolve().parent.parent
    failures = validate(package_root)
    if failures:
        for failure in failures:
            print(f'ERROR: {failure}')
        sys.exit(1)
    print('PASS: package files, UTF-8, metadata, relative references, portability')
