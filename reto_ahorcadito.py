import os
from random import randint



def archivo():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [line for line in f]
        # print(words)

    choosen_word = words[randint(0,len(words))]
    print(choosen_word)
    print(len(choosen_word)* "-")




def run():

    os.system("clear")

    print("""
                        ¡¡¡¡JUEGO DEL AHORCADO!!!
    ------------------------------------------------------------------------------
    """)
    letra = input("Ingresa una letra: ")
    pass

if __name__ == "__main__":
    archivo()

