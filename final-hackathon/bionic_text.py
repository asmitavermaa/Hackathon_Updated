import PyPDF2

def make_first_half_bold(text):
    words = text.split()
    result = ""

    for word in words:
        if len(word) > 1:
            half_len = len(word) // 2
            bold_word = "<b>" + word[:half_len] + "</b>" + word[half_len:]
            result += bold_word + " "
        else:
            result += word + " "

    return result.strip()

def convert_to_half_bold(input_pdf_path, output_html_path):
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    text = ""

    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()

    half_bold_text = make_first_half_bold(text)

    
    with open(output_html_path, "w", encoding="utf-8") as output_file:
        output_file.write(half_bold_text)

    print("HTML conversion complete. Output saved as", output_html_path)

if __name__ == "__main__":
    input_pdf_path = input("Enter the path to the input PDF file: ")
    output_html_path = input("Enter the desired output HTML file name: ")

    convert_to_half_bold(input_pdf_path, output_html_path) 