from ebooklib import epub
from bs4 import BeautifulSoup

class Epub:

    def __init__(self, file_path):
        self.file = epub.read_epub(file_path)

    def retrive_text(self):
        new_text = ""
        for i in self.file.items:
            if "html" in i.media_type:
                soup = BeautifulSoup(i.get_content(), "html.parser")
                new_text += f"\n {soup.get_text()}"
        return new_text

    def split_document(self, beg, end):
        pass