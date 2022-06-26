from googletrans import Translator
from langs import Langs


class TranslateWordsWritten:
    """ Translates spoken words into desired language --> string only """

    def __init__(self, text):
        """
        Initiates written word class
        :param text: spoken string from speech method
        """
        self.text = text

    def trans(self):
        """ Takes imported language destination and uses translate function from Translator class in googletrans"""
        translator = Translator()
        lin = Langs()
        try:
            t1 = translator.translate(self.text, dest=lin.which_lang_string())
            return f'{self.text} -----> {t1.text}'      # returns spoken text as well as translated text
        except:
            print("This is an invalid input for a language! Would you like to see the possible ones to choose from?")