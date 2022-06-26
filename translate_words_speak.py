import os

from langs import Langs
from gtts import gTTS
from googletrans import Translator


class TranslateWordsSpoken:
    """ Translates spoken words into desired language --> vocal and written translation """

    def __init__(self, text):
        """
        Initializes the spoken words class
        :param text: translated string from speech method
        """
        self.text = text

    def transl_voice(self):
        """ Takes the inputs from the Langs class and sets them into the correct destination/tld"""
        translator = Translator()
        lin = Langs()
        l = lin.which_lang_string()
        t = lin.which_lang_voice()

        t1 = translator.translate(self.text, dest=l)    #translates the string to the selected language
        txt = gTTS(t1.text, lang=l, tld=t)      #takes translated string and adds specified accent by language code
        print(f'{self.text} ------> {t1.text}')
        u = input("How would you like to name this file?: ")

        # saves and opens audio file
        txt.save(u + ".mp3")
        os.system(u + ".mp3")

        return ""
