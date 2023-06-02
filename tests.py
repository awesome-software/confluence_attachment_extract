import unittest

from confluence_attachment_extract import getsoup, getspacename, getattachments


# def main(dir='', copyfile=True, images=False):
#     attachmentfilemap = getmap(dir)
#     if copyfile:
#         os.makedirs(f'{dir}/attachment', exist_ok=True)
#
#     with open(f'{dir}/entities.xml', 'r') as f:
#         file = f.read()
#     soup = BeautifulSoup(file, 'xml')
#     attachments = soup.find_all('object', {'class': 'Attachment'})
#
#     filenamemap={}
#     for att in attachments:
#         id = att.find('id')
#         title = att.find('property', {'name': 'title'})
#         filenamemap[str(id.text)]=title.text
#
#     pages = soup.find_all('object', {'class': 'Page'})
#     for page in pages:
#         id = page.find('id')
#         title = page.find('property', {'name': 'title'})
#         atts = page.find_all('element', {'class': 'Attachment'})
#         if len(atts) > 0:
#             print('-'*20)
#             print(id.text, title.text, len(atts))
#             for att in atts:
#                 attid=att.find('id')
#                 print(attid.text, filenamemap[str(attid.text)])
#                 print(f"attachments/{id.text}/{attid.text}")
#                 src=f"{dir}/attachments/{id.text}/{attid.text}/1"
#                 dst=f"{dir}/attachment/{title.text}/{filenamemap[str(attid.text)]}"
#                 import filetype
#                 try:
#                     kind = filetype.guess(src)
#                 except:
#                     print(f"no {src}")
#                     continue
#                 if kind is not None and kind.mime.startswith('image/') and not images:
#                     continue
#                 try:
#                     os.makedirs(f'{dir}/attachment/{title.text}', exist_ok=True)
#                     shutil.copyfile(src,dst)
#                 except:
#                     print(f" cant copy {dir}/attachments/{id.text}/{attid.text}/1", f"{dir}/attachment/{title.text}/{filenamemap[str(attid.text)]}" )
#             print()
#
#
#
# def main2(dir=''):
#     attachmentfilemap = getmap(dir)
#     with open(f'{dir}/entities.xml', 'r') as f:
#         file = f.read()
#     soup = BeautifulSoup(file, 'xml')
#     ids = soup.find_all('property', {'name': 'title'})
#     for elem in ids:
#         prev = elem.find_previous_sibling('id')
#         if prev.text in attachmentfilemap.keys():
#             pass
#             print(prev.text, elem.text)
#
#
# def getmap(dir=''):
#     attachmentfilemap = {}
#     for root, dirs, files in os.walk(f"{dir}/attachments", topdown=False):
#         for name in files:
#             if '173889627' in name:
#                 print(root, files)
#             atoms = root.split('/')
#             attachmentfilemap[atoms[-1]] = f"{root}/{name}"
#     return attachmentfilemap


class MyTestCase(unittest.TestCase):

    @unittest.skip('expensive')
    def test_soup(self):
        dir = '/Users/trice/Downloads/Confluence-space-export-221752-538.xml'
        soup = getsoup(dir)
        self.assertTrue(soup is not None)

    def test_spacename(self):
        dir = '/Users/trice/Downloads/Confluence-space-export-221752-538.xml'
        soup = getsoup(dir=dir)
        spacename = getspacename(soup)
        self.assertEqual(spacename, 'Space name')
        getattachments(spacename, dir, soup, images=False)

    def test_something(self):
        main(dir='/Users/trice/Downloads/Confluence-space-export-235052-450.xml')


if __name__ == '__main__':
    unittest.main()
