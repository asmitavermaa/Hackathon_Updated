import requests
import json

url = "https://api.worqhat.com/api/ai/content/v2"

headers = {
    "Authorization": "Bearer sk-8a421eeaabac4f8cb91ab4ec742562fe",
    "Content-Type": "application/json"
}

def ask_chatbot(question, conversation_history, randomness=0.4):

    payload = {
        "question": question,
        "preserve_history": True, 
        "randomness": randomness,
        "training_data": conversation_history 
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        return response_data["content"]
    else:
        return "Error: Failed to get a response from the chatbot."

def main():
    print("Chatbot: Hello! I am here to answer you questions on anything you would like to know about Attention Deficit Hyperactivity Disorder (ADHD)")

    with open("document.txt", "r") as file:
        document_content = file.read()

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            break
        
        chatbot_response = ask_chatbot(user_input, document_content)
        print(f"Chatbot: {chatbot_response}")


if __name__ == "__main__":
    main()