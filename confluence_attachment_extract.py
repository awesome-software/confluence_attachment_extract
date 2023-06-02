#!/usr/bin/env python3
import argparse
import os
import shutil

import filetype
from bs4 import BeautifulSoup


def getsoup(dir):
    with open(f'{dir}/entities.xml', 'r') as f:
        file = f.read()
    soup = BeautifulSoup(file, 'xml')
    return soup


def getspacename(soup):
    space = soup.find('object', {'class': 'Space'})
    name = space.find('property', {'name': 'name'})
    return name.text


def getattachments(spacename, directory, soup, copyfile=True, images=False, verbose=False):
    print(spacename, directory)
    if copyfile:
        os.makedirs(f'{directory}/{spacename}', exist_ok=True)

    attachments = soup.find_all('object', {'class': 'Attachment'})

    filenamemap = {}
    for att in attachments:
        id = att.find('id')
        title = att.find('property', {'name': 'title'})
        filenamemap[str(id.text)] = title.text

    pages = soup.find_all('object', {'class': 'Page'})
    missingfiles = set()
    for page in pages:
        id = page.find('id')
        title = page.find('property', {'name': 'title'})
        atts = page.find_all('element', {'class': 'Attachment'})
        if len(atts) > 0:
            if verbose:
                print('-' * 20)
                print(f"{title.text} ({id.text}) has {len(atts)} attachment(s)")
            for att in atts:
                attid = att.find('id')
                if verbose:
                    print(f"  {filenamemap[str(attid.text)]}")
                src = f"{directory}/attachments/{id.text}/{attid.text}/1"
                dst = f"{directory}/{spacename}/{title.text}/{filenamemap[str(attid.text)]}"
                try:
                    kind = filetype.guess(src)
                except:
                    missingfile = f" {filenamemap[str(attid.text)]} on the {title.text} page"
                    missingfiles.add(missingfile)
                    continue
                if kind is not None and kind.mime.startswith('image/') and not images:
                    continue
                try:
                    os.makedirs(f'{directory}/{spacename}/{title.text}', exist_ok=True)
                    shutil.copyfile(src, dst)
                except:
                    print(f" cant copy {directory}/attachments/{id.text}/{attid.text}/1",
                          f"{directory}/attachment/{title.text}/{filenamemap[str(attid.text)]}")
            print()
    if len(missingfiles) > 0:
        print("the following attachments were not found in the export:")
        print("\n".join(missingfiles))


def main():
    parser = argparse.ArgumentParser(
        prog='confluence_attachment_extract',
        description='extracts attachment files from a Confluence XML dump')
    parser.add_argument('directory')
    parser.add_argument('-v', '--verbose', action='store_false', help='more output')  # on/off flag
    parser.add_argument('-i', '--images', action='store_false',
                        help='include image files, usually not necessary when also exporting a PDF')  # on/off flag
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        raise IsADirectoryError(f"{args.directory} is not a directory")
    soup = getsoup(dir=args.directory)
    spacename = getspacename(soup)
    if args.verbose:
        print(f"extracting images from the {spacename} space from an XML dump in {args.directory}")
    getattachments(spacename, args.directory, soup, images=args.images, verbose=args.verbose)


if __name__ == '__main__':
    main()
