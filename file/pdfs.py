from PyPDF2 import PdfReader


class PDF:

    def __init__(self, file_path):
        self.new_text = ""
        with open(file_path, 'rb') as file:
            self.file = PdfReader(file)
            for num in range(len(self.file.pages)):
                page = self.file.pages[num]
                self.new_text += page.extract_text()
        # print(self.new_text)