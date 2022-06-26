import speech_recognition as sr
# imports the speech_recognition package to access the microphone class and functions


def speech():
    """ A function that recognizes the users voice and translates it into a string"""

    r = sr.Recognizer()     # initiates the recognizer class
    with sr.Microphone() as source:     # opens microphone as a listening object
        print("Speak into the microphone:")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)    # google recognition services return a string translation of audio
    except sr.UnknownValueError:
        print("The audio was not understood")
