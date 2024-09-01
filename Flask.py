from flask import Flask, request, jsonify, render_template
import openai

openai.api_key = 'your-openai-api-key'  # Replace with your OpenAI API key

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # You'll create this HTML file to handle input/output

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = chat_with_gpt(user_input)
    return jsonify(response=response)

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
