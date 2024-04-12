from dotenv import load_dotenv
import os

load_dotenv()

class Silencer:

    def __init__(self, file_path, file_type):
        if not(os.path.exists(file_path)):
            print("File does not exist")
            return
        if file_type == "pdf":
            self.text = self.call_pdf(file_path)
        elif file_type == "epub":
            self.text = self.call_epub(file_path)
        elif file_type == "dju":
            self.text = self.call_dju(file_path)
        else:
            print("File path is inexistent")
            pass    
        self.adjust()
        print(self.all_text)
        # self.convert_to_audio(self.all_text)

    def adjust(self):
        self.text = self.text.split(".")
        self.all_text, t = [], ""
        for i in self.text:
            if len(t + i) < 12000:
                t += i
            else:
                self.all_text.append(t)
                t = ""
        self.all_text.append(t)

    def call_pdf(self, file_path):
        from file.pdfs import PDF
        pdf = PDF(file_path)
        # print(pdf.new_text)
        return pdf.new_text

    def call_epub(self, file_path):
        from file.epub import Epub
        epub = Epub(file_path)
        return epub.retrive_text()

    def call_dju(self, file_path):
        pass

    def convert_to_audio(self, text):
        from pyht import Client
        from pyht.client import TTSOptions
        from file.audio import Audio


        client = Client(
            user_id=os.getenv("PLAY_HT_USER_ID"),
            api_key=os.getenv("PLAY_HT_API_KEY"),
        )
        audio = Audio()
        options = TTSOptions(voice="s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json")
        for i in self.all_text:
            for chunk in client.tts(i, options):
                audio.append_song(chunk)
                print(type(chunk))


if __name__ == "__main__":
    # sound = Silencer("C:/Users/Dilibe/Downloads/flask-cors-readthedocs-io-en-latests.epub", 'epub')
    sound = Silencer("C:/Users/Dilibe/Downloads/Second resume.pdf", 'pdf')
