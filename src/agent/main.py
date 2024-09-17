from dotenv import load_dotenv
load_dotenv()

import os
import requests
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def chat_with_model(deployment_name, messages):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages
    )
    return response.choices[0].message.content

def get_prompt_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error fetching prompt from URL: {e}")
        return None

def main():
    deployment_name = "ip-gpt-4o"
    print(f"Using deployment: {deployment_name}")

    default_system_message = "You are a helpful assistant that can answer questions and help with tasks."
    
    prompt_url = input("Enter URL for a specific instruction set (or press Enter to use default): ").strip()
    
    if prompt_url:
        system_message = get_prompt_from_url(prompt_url)
        if not system_message:
            print("Failed to fetch prompt from URL. Using default prompt.")
            system_message = default_system_message
    else:
        system_message = default_system_message

    print(f"Using system message: {system_message}")

    messages = [
        {"role": "system", "content": system_message},
    ]

    print("\nWelcome to the AI chat!")
    print("You can exit the conversation by typing 'exit' or pressing Ctrl+C.")

    try:
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            messages.append({"role": "user", "content": user_input})

            try:
                response = chat_with_model(deployment_name, messages)
                print("Assistant:", response)
                messages.append({"role": "assistant", "content": response})
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print("Let's try again.")
    except KeyboardInterrupt:
        print("\nConversation ended by user. Goodbye!")

if __name__ == "__main__":
    main()
