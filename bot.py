import openai

# Initialize OpenAI API key
openai.api_key = 'your-openai-api-key'  # Replace with your OpenAI API key

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Hello! I am an AI chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
