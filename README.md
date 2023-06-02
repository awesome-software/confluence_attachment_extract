# Confluence Attachment Extract

Of the export options available for Confluence sites (XML, HTML and PDF), only
XML (Atlassian also calls this "back-up") includes all attachments to pages.
HTML and PDF include the image attachments but not any other filetype. This makes it challenging to migrate Confluence
spaces anywhere but another Confluence instance or even export the contents of a Confluence space or reference outside
of Confluence.

The zip file contains an XML file and attachment files. Those files are in a directory tree
named by the numeric id of file and the id of the page its attached to. This directory structure
is not human readable nor does it include any information about the filetype.

This small script parses the XML file and copies attachment files by their original filename into a a directory named
for
the parent page.

## Syntax

```confluence_attachment_extract.py  <confluence xml export directory>```

## Usage

Requirements: admin level permissions on the Confluence server

1. Export a Confluence space using the XML option ([see Atlassian's documentation for guidance](https://confluence.atlassian.com/doc/export-content-to-word-pdf-html-and-xml-139475.html)  
2. Save the resulting zip file locally, the unzip it.
3. run the script 

Example:```confluence_attachment_extract.py ~/Downloads/Confluence-export-12345-789.xml```


4. A directory will be created with subdirectories for each page with an attachment.  Those attachments will be copied in to those directories with their original filenames.  