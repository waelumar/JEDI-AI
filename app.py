from flask import Flask, request, render_template, url_for
from gemini_handler import get_gemini_response
from tts_handler import text_to_speech
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jedi', methods=['GET', 'POST'])
def jedi():
    if request.method == "POST":
        user_input = request.form['message']
        character = request.form.get('character', 'jedi knight')

        ai_response = get_gemini_response(user_input, character)

        # Generate voice audio
        text_to_speech(ai_response)

        return render_template("jedi.html",
                               user_input=user_input,
                               ai_response=ai_response,
                               character=character,
                               timestamp=datetime.now().timestamp())
    return render_template('jedi.html', ai_response=None, timestamp=datetime.now().timestamp())

if __name__ == '__main__':
    app.run(debug=True)
