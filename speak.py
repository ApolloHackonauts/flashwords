#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
from Languages import langs

import speech_recognition as sr

def speech_to_text(lang= "en-US"):

    lang =  lang.lower()

    if lang in langs:
        lang = langs[lang]

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Cloud Speech
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
    "type": "service_account",
    "project_id": "seventh-odyssey-201902",
    "private_key_id": "cd162040164d6c5aa266db7a9f9a3b4d6099e0e3",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC8Y7JrhP8JVhTr\nsw98G2aqwrZEKxKSJuMwN2NaIPz6vR9iNOHqPL4d3tSGdY7M+RnHuq7MhJaLByYV\nnDtauAiZkfgiXuXncNapb257EFWMAV/dpsFXiYIAREnQyC2m0bQv1uxDcgls05id\nxaX6mw4wcdOiUl3WT5RylZ2ZhL4HjS4ohhZSuEgI7g4q/kJ4sE8eFEvk/PPVBIEH\nfLQJWwnv+E7gF/BkhF15hiYDcXT7pYigJd3tChpa877Dw5i3Ww9maa12ucCPoq6J\nVqUewhYR85DlFwoNsfAdS5+dB81tv/sY7Lubi1W7mRWrkRwogrAVZMR95nAbuTb3\nyuiIoq9nAgMBAAECggEAJULo3tha41tZ3va3ONpol5zUlS4ZybuUUwyZg5Gjx+pR\nQ0jnaD+kcN8KlR+6Y3NftIAJo90Ts6Lx1vNkUAC3frx+4jl36quIYdHu/btQ2FTL\nQ9mAQ1Ko2mmnWfrGAMlYhN/TMlHjaFl/xbD6r9MsXsucyu3Urpdl6rYKCnvVZEOi\nVQy4lg/gD90l32ntPb8TRB3rKEEFs704eh/Gs4rJ0PRqUWhO4ViUQvH6AW1pfT4G\nkZ2AOMgMRcyqu4MTuzjtYJaXusba668hhCWjA9goDt6yPkOVLx65QnOarbmBpmfa\ng93zGCHUEEb72Ufzds2ddRX72BusHrnXKR9r5E/7RQKBgQD4cK+mmYKhYUmb6vkJ\nddgFZx87V7c8WWnhNY0T5Ofqj5lPLUsRsN4EZDDZt/+hOxe5HCuxZFbM2wlE+CN1\nZVfRlFUkaMefxxsouTi4/g4HbCGOb8/BJn2oE486wbUN6kT33Xo4bD6tQ3mnh76+\ny7IIiHin7tL6BlyslZd9t5hj+wKBgQDCHzlbnPWAvcwCYQuPJOf39/ffnp5XrIZE\ntbgdIRevq3QJSktjUzH0GEz+ksVRoYmT/5EcbEGQydk5YS5CQvXopEW5e3a4hq8s\n4GCcy5cn9La0ON5tURoG8OJW8l3yy1kazHJ7zALwppeF6a8O2qpvO0AWPMA2q6d9\nxj/CoInahQKBgDD1a/gF2nNZC7t5M7iEi5yM9N+p6ocvC6mA9xtLidR0lf6/a0LC\nOw5cfC/7jZnFXmhxP78GigB2zb3UtJAm94Zql9jD+UroXtbIoX/7OOKHkZlTOXrT\nzgF4UUp/7+EdIJhEAhjqY/ObD3dPTeylkaES28wkSVlSNaMhG6h/rL1PAoGAMVXe\nLfpmKqISB0jCt06Z5duPk7WsaHvgY/YLJNwUOQFKLFJFdqjeOTsz1j9XBrgXTxXU\nu3SH9VRXcM3SA+Uguk+FqO5H7f3M54rfAvp7IByBkqwhW4cRJlJyM8bFOb+UlcsA\nDZZ76M1uFQqfAxdv2XUlhIFMGJjnqH+KFNzYLEECgYEAtMx60Z//+hYqeLJ6uQiT\nXJobsjUgDcLp/pyi4L8JQAej6oUnsXX5+xej3URFfYib2WfGW1ZHKi1ZTeD9L8z1\nr+R+aLv7WEB4Ktm5gt2CTx69QTqeA2P8EqFfUOZNuG+uhyNE9OgFfJgN1SWbm+tI\nkaEvE8SFITYEuOoHqDxYHhE=\n-----END PRIVATE KEY-----\n",
    "client_email": "starting-account-6dx7jylzv230@seventh-odyssey-201902.iam.gserviceaccount.com",
    "client_id": "110407418298771212261",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/starting-account-6dx7jylzv230%40seventh-odyssey-201902.iam.gserviceaccount.com"
    }"""

    try:
        return r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language=lang)
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))


if __name__ == "__main__":
    
    speech = speech_to_text("spanish")
    print("Google thinks you said, " + speech)

    



