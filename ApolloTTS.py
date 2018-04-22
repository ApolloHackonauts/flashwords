#TODO -- add console output logging
from Languages import langs

def synth_text(text, lang='en-US'):
    """Send raw text to be synthesized into audio
    input:  text : str
            lang : str
    output: output.mp3
    lang must be a valid language code, i.e. 'en-US'
    """
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=lang,
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

if __name__ == '__main__':
    synth_text('Yes! Soylent has arrive! Gib right now I want it-I want it!', langs['english'])