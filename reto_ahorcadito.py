import os
from random import randint

# def archivo():
#     with open("./archivos/data.txt", "r", encoding="utf-8") as f:
#         words = [line for line in f]
#         # print(words)

#     choosen_word = words[randint(0,len(words))]
#     print(choosen_word)
#     print(len(choosen_word))
#     print(len(choosen_word)* "-")

def run():
    os.system("clear")
    print("""
                        ¡¡¡¡JUEGO DEL AHORCADO!!!
    ****************************************************************************
    Se te muestra una cadena de texto de modo que sepas cuantos carácteres tiene la palabra que debes adivinar. Tienes X intentos
    """)
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [line for line in f]
        # print(words)
    choosen_word = words[randint(0,len(words))]
    print(choosen_word)
    # print(len(choosen_word))
    word_in_code = [ " _ " for i in range(0, len(choosen_word)-1)]
    # word_in_code =  [(len(choosen_word)- 1) * "-"]
    print((len(choosen_word)- 1) * " _ ")
    # print(word_in_code)
    x = True 
    word_in_list = ""
    

    while x == True:

        letter = input("Ingresa una letra: ").lower()
        for i in range(0,len(choosen_word)):
            if choosen_word[i] == letter:
                word_in_code[i] = letter

        # for lett in word_in_code:
        #     word_in_list += lett

        print(word_in_list)
        if " _ " in word_in_code:
            x = True
        else:
            x = False
            print("Lo lograste!!! Fuiste capaz de adivinar la palabra!")
        


if __name__ == "__main__":
    run()

