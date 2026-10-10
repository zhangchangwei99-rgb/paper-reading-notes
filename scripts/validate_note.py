"""Check default Word output conventions; not factual or visual quality.

Python 3.10+, standard library only. Images of original tables are allowed.
"""
import argparse
from pathlib import Path
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
from zipfile import BadZipFile, ZipFile


NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'v': 'urn:schemas-microsoft-com:vml',
}
REL = '{http://schemas.openxmlformats.org/package/2006/relationships}'
FORBIDDEN_LABEL = re.compile(
    r'^(?:[一二三四五六七八九十\d]+[、.．]\s*)?'
    r'(?:研读版本|参考来源|参考文献|来源说明|核验记录|阅读覆盖范围)'
    r'(?:\s*[:：].*)?$'
)
FORMULA = re.compile(
    r'\\(?:\(|\[|begin\b|frac\b|sqrt\b|sum\b|mathrm\b|text\b|beta\b|alpha\b)'
    r'|\$[^$\n]+\$|[√∑∏∫]|[α-ωΑ-Ω]|[₀-₉]'
    r'|\b[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9{]'
    r'|\b[A-Za-z][A-Za-z0-9]*\s*[=＝]\s*[A-Za-z0-9]'
)


def validate(path):
    errors, warnings = [], []
    if path.suffix.lower() != '.docx':
        return ['Expected one .docx file'], warnings
    try:
        with ZipFile(path) as package:
            names = set(package.namelist())
            if not {'[Content_Types].xml', 'word/document.xml'} <= names:
                return ['Missing required Word package parts'], warnings
            main_text = []
            for part in sorted(names):
                if not (part.startswith('word/') and part.endswith('.xml')):
                    continue
                root = ET.fromstring(package.read(part))
                if root.find('.//w:tbl', NS) is not None:
                    errors.append(f'{part}: recreated Word table')
                if any(root.find(f'.//m:{tag}', NS) is not None
                       for tag in ('oMath', 'oMathPara')):
                    errors.append(f'{part}: equation object')
                for paragraph in root.findall('.//w:p', NS):
                    text = ''.join(
                        element.text or '' for element in paragraph.findall('.//w:t', NS)
                    )
                    text = text.strip()
                    if part == 'word/document.xml':
                        main_text.append(text)
                    if FORBIDDEN_LABEL.fullmatch(text):
                        errors.append(f'{part}: forbidden section label: {text[:40]}')
                    if FORMULA.search(text):
                        errors.append(f'{part}: possible formula or math variable: {text[:60]}')
                    if (re.match(r'^(?:#{1,6}\s|```|\|.+\|\s*$)', text)
                            or '**' in text or re.search(r'!\[[^\]]*\]\(', text)):
                        errors.append(f'{part}: residual Markdown: {text[:60]}')

                references = []
                for blip in root.findall('.//a:blip', NS):
                    if blip.get(f'{{{NS["r"]}}}link'):
                        errors.append(f'{part}: external image link')
                    references.append(blip.get(f'{{{NS["r"]}}}embed'))
                for image in root.findall('.//v:imagedata', NS):
                    references.append(image.get(f'{{{NS["r"]}}}id'))
                if not references:
                    continue
                directory, filename = posixpath.split(part)
                relpart = posixpath.join(directory, '_rels', filename + '.rels')
                relationships = {}
                if relpart in names:
                    relationships = {
                        item.get('Id'): item
                        for item in ET.fromstring(package.read(relpart)).findall(REL + 'Relationship')
                    }
                for ref in references:
                    item = relationships.get(ref)
                    if not ref or item is None:
                        errors.append(f'{part}: missing image relationship: {ref}')
                        continue
                    if item.get('TargetMode') == 'External':
                        errors.append(f'{part}: image is not embedded: {ref}')
                        continue
                    target = item.get('Target', '')
                    resolved = (posixpath.normpath(target).lstrip('/') if target.startswith('/')
                                else posixpath.normpath(posixpath.join(directory, target)))
                    if not item.get('Type', '').endswith('/image') or resolved not in names:
                        errors.append(f'{part}: missing embedded image: {ref}')
            count = len(re.findall(r'[\u4e00-\u9fff]', '\n'.join(main_text)))
            if count > 4500:
                warnings.append(
                    f'{count} Chinese characters including metadata/captions; review repetition and selection'
                )
    except (OSError, BadZipFile, ET.ParseError) as error:
        errors.append(f'Cannot inspect Word package: {error}')
    return list(dict.fromkeys(errors)), warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('document', type=Path, help='Final .docx to inspect')
    args = parser.parse_args()
    errors, warnings = validate(args.document)
    for warning in warnings:
        print(f'REVIEW: {warning}')
    for error in errors:
        print(f'ERROR: {error}')
    if errors:
        return 1
    print('PASS: Word format guards and embedded image references; verify facts and rendered pages separately')
    return 0


if __name__ == '__main__':
    sys.exit(main())
