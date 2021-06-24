from pwgenerator import *
import random

def askUserInput():
    global pwLength
    global reqNums
    global reqCharacters
    pwLength = int(input("Kui pikk on teie soovitud parool?"))
    reqNums= int(input("Kui palju on teie paroolis vaja numbreid?"))
    reqCharacters = int(input("Kui palju on teie paroolis vaja sümboleid?"))

    if (reqNums >= pwLength):
        print("Midagi läks valesti. Numbreid ei saa olla rohkem kui parooli pikkus!")
        askUserInput()

    if (reqCharacters >= pwLength):
        print("Midagi läks valesti. Sümboleid ei saa olla rohkem kui parooli pikkus!")
        askUserInput()
    print("Teie parool on ", generatePw())
    

def generatePw():
    password = []
    numOfLetters = pwLength - reqNums - reqCharacters
    for _ in range(numOfLetters):
        password.append(randomLetter())
    for _ in range(reqNums):
        password.append(randomNumber())
    for _ in range(reqCharacters):
        password.append(randomCharacter())
    random.shuffle(password)
    password = ' '.join(map(str,password))
    return password

askUserInput()
    
