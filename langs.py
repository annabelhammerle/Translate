from gtts.lang import _main_langs
# Here the main languages are encoded in the package as a dictonary
# This class calls the imported class, updates a new dictionary and (1) prints
# the possible languages or (2) returns an inputed languages for the destination in translate_words


class Langs:
    """ Prints the possible languages to choose from and sets destination for translating """
    def __init__(self):
        self.dic_langs = {}
        self.dic_langs.update(_main_langs())

    def print_langs(self):
        """ Prints the dictionary with <language>: <language code>"""
        print("The available languages to choose from are:")
        for key, value in self.dic_langs.items():
            print(f'{value}: {key}')

    def which_lang_string(self):
        """ Allows user to type the language name and returns the language code"""
        bol = False
        dect = ""
        lingua = input("Enter the language name you want to translate to: ")
        for key, value in self.dic_langs.items():
            if lingua.capitalize() in value:
                dect = key
                bol = True
                break
            else:
                bol = False

        if bol:
            return dect
        else:
            return None

    def which_lang_voice(self):
        """ Finds the language accent for the vocal translation """
        se1 = {"al", "bg", "bs", "de", "fi", "fr", "hr", "hu", "is", "it", "la", "lv", "mk", "ml", "ms", "ne", "no",
               "nl", "pl", "pt", "ro", "ru", "si", "sk", "sr", "tl"}
        se2 = {"af", "ar", "bn", "cy", "et", "my", "sv", "tr"}
        se3 = {"en", "es", "zh-CN"}
        d2 = {"sq": "al", "ca": "cn", "cs": "cz", "da": "dj", "eo": "com.ec", "el": "ee", "gu": "com.gi", "hi": "hn",
              "iw": "ht", "id": "co.id", "hy": "im", "jw": "je", "ja": "co.jp", "km": "com.kh", "ko": "co.kr",
              "kn": "com.kw", "sw": "com.sa", "su": "sn", "th": "co.th", "ta": "tm", "te": "to", "uk": "com.ua",
              "ur": "com.uy", "vi": "co.vi", "mr": "com.mt"}
        lingua = input("Enter which language accent you want to hear: ")
        for accent in se3:
            if lingua == accent:
                tld = "com"
                return tld
        for accent in se1:
            if lingua == accent:
                tld = lingua
                return tld
        for accent in se2:
            if lingua == accent:
                tld = "com." + lingua
                return tld
        for key, value in d2.items():
            if lingua == key:
                tld = value
                return tld
        else:
            raise ValueError("Choose a correct accent input")
