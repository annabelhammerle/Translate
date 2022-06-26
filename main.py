import os

from translate_words_write import TranslateWordsWritten
from translate_words_speak import TranslateWordsSpoken
from langs import Langs
from speech_re import speech

n = 1
while n != 0:
    print("========== Menu =========== \n" 
          "Would you like to: \n"
          "(1) View the available languages to choose from \n"
          "(2) Speak and receive a vocal and written translation \n" 
          "(3) Speak and receive a written translation \n"
          "(4) Play an existing audio file \n"
          "(0) Exit")
    n = int(input())

    if n == 1:
        lin = Langs()
        lin.print_langs()

    if n == 2:
        us = "t"
        while us != "y":
            sp = speech()
            print("Did you say:", sp, "? y/n")
            us = input()
        tran = TranslateWordsSpoken(sp)
        print(tran.transl_voice())
    if n == 3:
        us = "t"
        while us != "y":
            sp = speech()
            print("Did you say:", sp, "? y/n")
            us = input()
        tran = TranslateWordsWritten(sp)
        print(tran.trans())

    if n == 4:
        u = input("Which file are you looking for?: ")
        os.system(u + ".mp3")

    else:
        print("")
