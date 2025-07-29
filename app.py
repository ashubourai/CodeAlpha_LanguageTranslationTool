from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def translate_page():
    output_translation = ""
    detected_lang = ""
    input_text = ""
    target_language = ""

    if request.method == 'POST':
        input_text = request.form.get('text', '').strip()
        target_language = request.form.get('target_lang', '').strip()

        if input_text and target_language:
            try:
                result = translator.translate(input_text, dest=target_language)
                detected_lang = LANGUAGES.get(result.src, 'Unknown').title()
                output_translation = result.text
            except Exception as e:
                output_translation = f"Error: {str(e)}"
        else:
            output_translation = "Please fill in the text and select a target language."

    return render_template('index.html',
                           translated_text=output_translation,
                           detected_language=detected_lang,
                           user_input_text=input_text,
                           target_language=target_language)

if __name__ == "__main__":
    print("Language Translator App is running...")
    app.run(debug=True)
