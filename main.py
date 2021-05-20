import random
from hangman_art import stages, logo
from hangman_words import word_list
#from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
display = ['_' for x in chosen_word]

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    #clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    count = 0
    for letter in chosen_word:
      if letter == guess:
        display[count]=letter
      count += 1
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])