# ******************************************************************************
#  Escribir un script para jugar al ahorcado. Dada una lista de palabras elegir #  una aleatoriamente para adivinarla en 6 intentos!! Debe recordar las letras  
#  usadas. ¡Espero que te diviertas jugando!  
# ******************************************************************************

import random

def choose_word():
    words = ["lenguaje", "programacion", "codigo", "computadora", "inteligencia"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("¡Bienvenido al Juego del Ahorcado!")
    print("Tienes que adivinar la palabra. ¡Buena suerte!")

    while True:
        print("\nPalabra:", display_word(word, guessed_letters))
        guess = input("Adivina una letra: ").lower()

        if guess in guessed_letters:
            print("Ya has intentado esa letra. ¡Intenta otra!")
        elif guess in word:
            guessed_letters.append(guess)
            print("¡Correcto!")
        else:
            attempts -= 1
            print("Incorrecto. Te quedan {} intentos.".format(attempts))
            if attempts == 0:
                print("¡Oh no! Te has quedado sin intentos. La palabra era '{}'.".format(word))
                break

        if all(letter in guessed_letters for letter in word):
            print("¡Felicidades! ¡Has adivinado la palabra '{}'!".format(word))
            break

if __name__ == "__main__":
    main()
