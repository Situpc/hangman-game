
import random
import hangman_art
import hangman_words
word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
guess_check = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    if guess in guess_check:
        print("You've already played " + guess)
    guess_check += guess

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        

    #Check if user is wrong.
    if guess not in chosen_word:
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        print("The letter " + guess + " is not in the word.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])