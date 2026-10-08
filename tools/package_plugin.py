#!/usr/bin/env python3
"""Package the plugin only, excluding repository docs and build tools."""
import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = args.output.resolve()
    if output.suffix.lower() != '.zip':
        parser.error('Output must be a .zip file.')
    for folder in ('assets', 'skills'):
        if output.is_relative_to(root / folder):
            parser.error('Output must be outside assets/ and skills/.')
    paths = [root / 'plugin.json']
    for folder in ('assets', 'skills'):
        folder_path = root / folder
        paths.append(folder_path)
        paths.extend(folder_path.rglob('*'))
    for path in paths:
        if path.is_symlink():
            parser.error('Source must not be a symbolic link: ' + str(path.relative_to(root)))
    manifest = json.loads((root / 'plugin.json').read_text(encoding='utf-8'))
    publisher = manifest.get('extensions', {}).get('com.openai', {}).get('interface', {}).get('developerName')
    if not publisher:
        print('Note: developerName still needs the verified publisher name before submission.')
    files = [p for p in paths if p.is_file()]
    if output in files:
        parser.error('Output must not overwrite a source file.')
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
        for file in sorted(files):
            archive.write(file, file.relative_to(root))
    with ZipFile(output) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError('ZIP CRC check failed: ' + bad)
    print(f'Created {output} ({len(files)} files)')


if __name__ == '__main__':
    main()
