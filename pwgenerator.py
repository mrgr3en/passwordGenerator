import random

def randomLetter():
    lettersArr = []
    letters = open("alphabet.txt", "r")
    for l in letters:
        lettersArr = l.split()
    letters.close()
    randNum = random.randint(0, len(lettersArr) -1)
    letter = lettersArr[randNum]
    return letter

def randomNumber():
    randNum = random.randint(0,9)
    return randNum

def randomCharacter():
    charactersArr = []
    characters = open("characters.txt", "r")
    for c in characters:
        charactersArr = c.split()
    characters.close()
    randNum = random.randint(0,len(charactersArr) -1)
    character = charactersArr[randNum]
    return character


        
        