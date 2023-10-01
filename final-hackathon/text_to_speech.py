from gtts import gTTS
from PyPDF2 import PdfReader 

def pdf_to_mp3(pdf_path, mp3_output_path):

    pdf_reader = PdfReader(pdf_path)

    pdf_text = ''

    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    tts = gTTS(text=pdf_text, lang='en')

    tts.save(mp3_output_path)

    print(f"Text converted to speech and saved as {mp3_output_path}")

if __name__ == "__main__":

    pdf_file_path = input("Enter the path to the PDF file: ")

    mp3_output_path = input("Enter the desired MP3 audio output file name (e.g., output.mp3): ")

    if not mp3_output_path.endswith(".mp3"):
        mp3_output_path += ".mp3"

    pdf_to_mp3(pdf_file_path, mp3_output_path)
