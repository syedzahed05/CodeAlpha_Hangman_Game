import random

words = ["python", "computer", "programming", "developer", "hangman"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

display_word = ["_"] * len(word)

print("================================")
print("       HANGMAN GAME")
print("================================")

while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    if guessed_letters:
        print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if "_" not in display_word:
    print("\nCongratulations! You won!")
    print("The word was:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)

print("\nThank you for playing!")