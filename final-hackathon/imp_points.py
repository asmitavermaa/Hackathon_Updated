import requests
import json

url_extract = "https://api.worqhat.com/api/ai/v2/pdf-extract"
url_summary = "https://api.worqhat.com/api/ai/content/v2"
api_key = "sk-d591ba6b6c814956b45b4d9194c69b8e"

def summarize_text(extracted_text):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    body = {
        'question': "What are the important points in the following text?",
        'training_data': extracted_text,
        'preserve_history': False,
        'randomness': 0.4,
        'stream_data': False
    }
    response = requests.post(url_summary, headers=headers, json=body)
    if response.status_code == 200:
        json_response = response.json()
        summarized_content = json_response.get('content', '')
        return summarized_content
    else:
        return f"Failed to summarize text. Status code: {response.status_code}"

def extract_and_summarize(pdf_file_path):
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    files = {
        'file': (pdf_file_path, open(pdf_file_path, 'rb'), 'application/pdf')
    }
    response = requests.post(url_extract, headers=headers, files=files)
    if response.status_code == 200:
        json_response = response.json()
        extracted_content = json_response['content']
        summarized_content = summarize_text(extracted_content)
        with open('summary.txt', 'w', encoding='utf-8') as file:
            file.write(summarized_content)
        print("Content has been summarized and saved to 'summary.txt'")
    else:
        print(f"Failed to extract content from the PDF. Status code: {response.status_code}")

pdf_file_path = input("Enter the PDF file path: ")
extract_and_summarize(pdf_file_path)