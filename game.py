word = "blegh"
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
        guess = input("What is your guess?")
        print(generateHint(guess))
        if guess == word:
            print("Congratulations!")
            break

gameLoop()