Prerequisites
*  Python: Make sure you have Python installed (preferably version 3.7 or higher).

*  OpenAI API Key: Obtain an API key from OpenAI's website.

*  Install Required Libraries: You need to install the openai Python package.


How the Code Works:
*  API Key Initialization: You need to set up your OpenAI API key to authenticate your requests.
*  Function chat_with_gpt():
      -Takes user input as a prompt and sends it to the OpenAI API.
      -Retrieves the response and returns it as the chatbot's reply.
*  Main Loop:
      -Continuously takes input from the user.
      -Sends the input to the chat_with_gpt() function to get a response.
      -Outputs the chatbot’s response until the user types "exit".

Running the Chatbot:

*  Replace 'your-openai-api-key' with your actual OpenAI API key in the code.

*  Run the script in a terminal or command prompt:
         python your_script_name.py
*  Interact with the chatbot by typing your messages.
*  Type "exit" to end the conversation.

How to Run the Flask App
*  Start the Flask server:
        python your_flask_app.py
*  Open a browser and go to http://127.0.0.1:5000/ to interact with your chatbot.

