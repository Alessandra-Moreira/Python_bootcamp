from hangman_art import stages, logo
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

print(logo)

display = []
for letter in chosen_word:
    display += "_"

while end_of_game == False:
    guess = input("Adivinhe uma letra da palavra: ").lower()

    if guess in display:
        print(f"Você adivinhou a letra{guess}")

    # Verificar carta adivinhada
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if guess == letter:
            display[position] = letter

    # Verifica se o usuário está errado.
    if guess not in chosen_word:
        print(
            f"Você adivinhou {guess}, isso não está na palavra. Você perde uma vida.")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Você Perdeu!.")
    # Junte todos os elementos da lista e transforme em uma String.
    print(f"{' '.join(display)}")

    # Verifica se o usuário tem todas as letras.
    if "_" not in display:
        end_of_game = True
        print("Você Ganhou!")

    print(stages[lives])
