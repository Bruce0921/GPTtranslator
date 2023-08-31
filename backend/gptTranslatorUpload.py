from flask import Flask, request, jsonify, send_from_directory
import os
import openai

app = Flask(__name__, static_folder='../frontend')
openai.api_key = "UrGPTAPI"

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

def translate_text(text, source_lang, target_lang):
    print(f"Translating text: {text}, from {source_lang} to {target_lang}")  # Debugging line
    prompt = f"Translate the following text from {source_lang} to {target_lang}: {text}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

@app.route('/translate', methods=['POST'])
def translate():
    print("Translate function called")  # Debugging line
    data = request.json
    print(f"Received data: {data}")  # Debugging line
    text = data['sourceText']
    source_language = data['sourceLang']
    target_language = data['targetLang']
    try:
        translated_text = translate_text(text, source_language, target_language)
        return jsonify({"translatedText": translated_text})
    except Exception as e:
        print(f"An error occurred: {e}")  # Debugging line
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)