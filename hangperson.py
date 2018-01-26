import random
import sys


def getWord():
    return "secret"

def showBlankBoard():
    print()
    print("   ______")
    print("   |    |")
    print("   |")
    print("   |")
    print("   |")
    print("___|_")
    print("")
    print("")
    return

def showOneBoard():
    print()
    print("   ______")
    print("   |    |")
    print("   |    O")
    print("   |")
    print("   |")
    print("___|_")
    print("")
    print("")
    return

def showTwoBoard():
    print()
    print("   ______")
    print("   |    |")
    print("   |    O")
    print("   |   -|")
    print("   |")
    print("___|_")
    print("")
    print("")
    return

def showThreeBoard():
    print()
    print("   ______")
    print("   |    |")
    print("   |    O")
    print("   |   -|-")
    print("   |")
    print("___|_")
    print("")
    print("")
    return

def showFourBoard():
    print()
    print("   ______")
    print("   |    |")
    print("   |    O")
    print("   |   -|-")
    print("   |    /")
    print("___|_")
    print("")
    print("")
    return

def showFiveBoard():
    print()
    print("   ______")
    print("   |    |")
    print("   |    O")
    print("   |   -|-")
    print("   |    /\ ")
    print("___|_")
    print("")
    print("")
    return

def showSixBoard():
    print()
    print("   ______")
    print("   |    |")
    print("   |   ")
    print("   |   ")
    print("   |    ")
    print("___|_ _(:3] /)_")
    print("")
    print("")
    return

def gameOverScreen():
    print("############################")
    print("#######  Game  Over  #######")
    print("############################")
    return

def showBoard(turn):
    if turn == 0:
        showBlankBoard()
    elif turn == 1:
        showOneBoard()
    elif turn == 2:
        showTwoBoard()
    elif turn == 3:
        showThreeBoard()
    elif turn == 4:
        showFourBoard()
    elif turn == 5:
        showFiveBoard()
    else:
        showSixBoard()
        gameOverScreen()
        main()
    return

def generateAnswer(word):
    answer = []
    for i in range(len(word)):
        answer.append("_")
    return answer

def guessLetter():
    print("")
    letter = input("Please guess a letter: ")
    return letter.lower()

def showAnswer(word):
    print()
    for i in word:
        print(i, end=" ")
    return

def checkGuess(secretWord, answer, guess):
    flag = 0
    if secretWord.find(guess) != -1:
        for i, character in enumerate(secretWord):
            if character == guess:
                answer[i] = guess
        flag = 1
    return flag

def winScreen():
    print("############################")
    print("#######   You Win!   #######")
    print("############################")

def playGame():
    secretWord = getWord()
    answer = generateAnswer(secretWord)
    turn = 0
    while turn <= 6:
        showBoard(turn)
        showAnswer(answer)
        guess = guessLetter()
        while checkGuess(secretWord, answer, guess) != 0:
            print("That letter is in the word!")
            showBoard(turn)
            showAnswer(answer)
            guess = guessLetter()
            checkGuess(secretWord, answer, guess)
            if "_" not in answer:
                winScreen()
                return
            print("Sorry that is not in the word")
        turn +=1
    return

def main():
    again = "y"
    while again == "y":
        playGame()
        again = input("Would you like to play again?")
        again = again[0].lower()

if __name__ == '__main__':
    main()
