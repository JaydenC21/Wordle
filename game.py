import random

wordBank = ["blegh", "soare", "qwert", "lunic", "trope"]
word = random.choice(wordBank)
default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'

def generateHint(userGuess):
    color = default
    hint = ""
    for i in range(5):
        if (userGuess[i] == word[i]):
            color = green
        elif (userGuess[i] in word):
            color = yellow
        else:
            color = default
        hint = hint + color + userGuess[i] + default
    return hint

def gameLoop():
    guess = ""
    for i in range(6):
        guess = input("Attempt " + str(i+1) + "/6: What is your guess?")
        print(generateHint(guess))
        if guess == word:
            if i==0:
                print("Congratulations! You got it in 1 try!")
                break
            else:
                print("Congratulations! You got it in " + str(i+1) + " tries!")
                break
    if guess != word:
        print("The word was: " + word)
        print("Better luck next time!")
gameLoop()