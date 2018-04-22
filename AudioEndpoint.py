from flask import Flask, request
from speak import speech_to_text

app = Flask(__name__)

FILENAME = 'pronounciation_attempt.'

@app.route('/say', methods=['POST'])
def say():
    if request.method == 'POST':
        if request.data and request.headers['filetype']:
            print(request.headers)
            audio_file = FILENAME + request.headers['filetype']
            with open(audio_file, 'wb') as out:
                out.write(request.data)

            target_lang = request.headers['target_lang']
            speech_text = speech_to_text(audio_file, lang=target_lang)
            return speech_text
    # if request.method == 'POST':
    #     recording = request.files['audio_file']
    #     print('got here')

if __name__ == '__main__':
    app.run(debug=True, port=5000)