from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

def translate_text(text, target_language):
    prompt = f"Translate the following English text to {target_language}: '{text}'"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60
    )
    return response.choices[0].text.strip()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data['text']
    target_language = data['target_language']
    try:
        translated_text = translate_text(text, target_language)
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def home():
    return "Welcome to my translation service!"

if __name__ == '__main__':
    app.run(debug=True)
