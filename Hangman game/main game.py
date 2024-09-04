import random
import logoGame
import HangmanPicture

word_list = ["apple", "banana", "carrot", "dog", "elephant", "fox", "grape", "horse", "tuanhung", "jellyfish", "kiwi", "lemon", "mango", "nut", "orange", "pear", "quail", "rabbit", "strawberry", "tomato", "unicorn", "violet", "watermelon", "xylophone", "yogurt", "zebra"]

hangman = 6
print(HangmanPicture.stanges[hangman])

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
word_needed_find = []
for i in range(word_length):
    print("_", end = "")
    word_needed_find.extend("_")
print("\n")
temp_word = ""

while (hangman > 0):
    hangman -= 1
    if (word_length > 0):
        guess = input("Guess a letter: ").lower()
        if (temp_word == guess):
            print("You have already guessed this letter")
            hangman += 1
            continue
        count = 0
        for letter in chosen_word:
            count += 1
            if(letter == guess):
                word_length -= 1
                word_needed_find[count-1] = letter
                if (temp_word != letter):
                    hangman += 1
                temp_word = letter
        print(HangmanPicture.stanges[hangman])
        for word in word_needed_find:
            print(word, end = "")
        print("\n")
    else:
        print("You win!")
        break
if(hangman == 0):
    print("You lose!")
    print("The word is", chosen_word)


