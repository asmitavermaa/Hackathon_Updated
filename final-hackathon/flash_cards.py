import requests
import json
import re

def extract_text_from_pdf_api(pdf_file_path, api_key):
    extraction_endpoint = "https://api.worqhat.com/api/ai/v2/pdf-extract"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    with open(pdf_file_path, "rb") as pdf_file:
        pdf_content = pdf_file.read()

    response = requests.post(extraction_endpoint, headers=headers, files={"file": ("document.pdf", pdf_content)})

    if response.status_code == 200:
        extraction_data = json.loads(response.text)
        extracted_content = extraction_data["content"]
        return extracted_content
    else:
        print(f"Failed to extract content from the PDF using the API. Status code: {response.status_code}")
        return None

def generate_questions(text):
   
    sentences = re.split(r'(?<=[.!?])\s', text)
    
    questions = []

    for sentence in sentences:
        
        if "explain" in sentence.lower():
            
            questions.append(f"Can you explain the following: '{sentence}'?")
        elif "compare" in sentence.lower() or "contrast" in sentence.lower():
           
            questions.append(f"Compare and contrast the elements in the following: '{sentence}'?")
        else:
           
            questions.append(f"What is the main idea of the following: '{sentence}'?")

    return questions

def extract_answers(text, questions):
    answers = {}
    
    sentences = re.split(r'(?<=[.!?])\s', text)

    for idx, question in enumerate(questions, 1):
        
        answer = "Answer not found."

        for sentence in sentences:
            if question.lower() in sentence.lower():
                answer = sentence
                break

        answers[idx] = answer

    return answers

if __name__ == "__main__":
    pdf_file_path = input("Enter the path to the PDF file: ")

    api_key = "sk-a141837e86a44562aa591ea6e461dd21"

    pdf_text = extract_text_from_pdf_api(pdf_file_path, api_key)

    if pdf_text:
        questions = generate_questions(pdf_text)
        answers = extract_answers(pdf_text, questions)

        print("Welcome to the Question Generator!")
        print("Click on each question to reveal the answer. Press 'Enter' to go to the next question.")

        for idx, question in enumerate(questions, 1):
            input(f"Question {idx}: {question}\nPress Enter to reveal the answer.")
            answer = answers.get(idx, "Answer not found.")
            print(f"Answer: {answer}\n")
