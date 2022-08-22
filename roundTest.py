### test function wofTurn
from itertools import cycle
import random
from config import dictionaryloc
### data structures needed for test

roundNum = 0 # number for rounds 1,2,3
roundWord = ""
blankWord = []
wheelList = ['BANKRUPT', 'LOSE A TURN', 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
players={0:{"roundtotal":0,"gametotal":0,"name":"Bad Bunny"},
         1:{"roundtotal":0,"gametotal":0,"name":"Karol G"},
         2:{"roundtotal":0,"gametotal":0,"name":"Lizzo"},
        }
vowels = {"a", "e", "i", "o", "u"}

def readDictionaryFile():
    #global dictionary
    # Read dictionary file in from dictionary file location
    # Store each word in a list.
    f = open(dictionaryloc)
    dicty = f.read()
    f.close()
    return dicty.split(', ')

dictionary = readDictionaryFile()

def getWord():
    global dictionary
    #choose random word from dictionary
    #make a list of the word with underscores instead of letters.
    roundWord = random.choice(dictionary).upper()
    roundUnderscoreWord = ['_' for x in range(len(roundWord))]
    return roundWord,roundUnderscoreWord

def wofRoundSetup():
    global players
    global roundWord
    global blankWord
    # Set round total for each player = 0
    for key in players.keys():
        players[key]['roundtotal'] = 0
    # Return the starting player number (random)
    #initPlayer = random.choice([1,2,3])
    # Use getWord function to retrieve the word and the underscore word (blankWord)
    roundWord, blankWord = getWord()
    return #initPlayer

def guessLetter(letter, playerNum):
    global players
    global blankWord
    global roundWord
    # parameters:  take in a letter guess and player number
    guessLetter = letter.upper()
    print(f'guessLetter:{guessLetter}')
    print(f'roundWord: {roundWord}')
    num = playerNum
    count = 0 # count correct letters in word from guessLetter
    # Change position of found letter in blankWord to the letter instead of underscore and update global blankWord with correctly guessed letters
    for i, v in enumerate(roundWord):
        if guessLetter == v:
            count += 1
            blankWord[i] = guessLetter
    # return goodGuess= true if it was a correct guess
    if count > 0:
        goodGuess = True
    else: goodGuess = False
    # return count of letters in word.
    ##### To Do: ensure letter is a consonate. #####
    
    print(blankWord)
    return goodGuess, count

def spinWheel(playerNum):
    global wheelList
    global players
    global vowels

    #set stillinTurn to true
    stillinTurn = True
    # Get random value for wheellist
    wheelResult = random.choice(wheelList)
    print(f'Wheel result is: {wheelResult}')
    # Check for bankrupcy, and take action.
    if wheelResult == 'BANKRUPT':
        stillinTurn = False ##### Set roundTotal to zero?
    # Check for lose turn
    elif wheelResult == 'LOSE A TURN':
        stillinTurn = False
    # Get amount from wheel if not lose turn or bankruptcy
    else:
    # Ask user for letter guess
        letter = input('Enter letter guess: ').upper()
    # Use guessletter function to see if guess is in word, and return count of correct letter in word
        goodGuess, count = guessLetter(letter, playerNum)
    # Change player round total if they guess right. Else end the turn
        if goodGuess == True:
            players[playerNum]["roundtotal"] += wheelResult
            players[playerNum]["gametotal"] += wheelResult
            print(f'Correct! There are {count} {letter}\'s in the word.')
        else:
            stillinTurn = False
            print('Incorrect guess.')
    print(f'Player totals after this turn are : {players}')
    return stillinTurn


### function wofTurn (only spin wheel option available)

def wofTurn(playerNum):  
    global roundWord
    global blankWord
    global roundNum
    global players

    # take in a player number. 
    # use the string.format method to output your status for the round
    # and Ask to (s)pin the wheel, (b)uy vowel, or G(uess) the word using
    # Keep doing all turn activity for a player until they guess wrong
    # Do all turn related activity including update roundtotal 
    
    stillinTurn = True
    while stillinTurn:
         
        # print blankWord and roundWord for debugging  
        print(f'blankWord: {blankWord}, roundWord: {[x for x in roundWord]}')
        # use the string.format method to output your status for the round
        print(f'Round status is: Round {roundNum}, Player {playerNum}\'s turn.')
        # Get user input S for spin, B for buy a vowel, G for guess the word
        choice = input(f'Player {playerNum}, would you like to (s)pin the wheel, (b)uy vowel, or G(uess) the word?')
                
        if(choice.strip().upper() == "S"):
            stillinTurn = spinWheel(playerNum)
        elif(choice.strip().upper() == "B"):
            stillinTurn = buyVowel(playerNum)
        elif(choice.upper() == "G"):
            stillinTurn = guessWord(playerNum)
        else:
            print("Not a correct option")      
        # Check to see if the word is solved, and return false if it is,
        if blankWord == [x for x in roundWord]:
            stillinTurn = False
            print('Word solved!')        
    # Or otherwise break the while loop of the turn.

def wofRound():
    global players
    global roundWord
    global blankWord
    global roundstatus
    #initPlayer = wofRoundSetup()
    wofRoundSetup()
    playerNums = [1,2,3]
    random.shuffle(playerNums)
    players_cycle = cycle(playerNums)
    # Keep doing things in a round until the round is done (word is solved)
    
    
    wordnotSolved = True
    while wordnotSolved:
        # While still in the round keep rotating through players
        wofTurn(next(players_cycle)-1)
        # Use the wofTurn fuction to dive into each players turn until their turn is done.
        # end loop if word is solved
        if blankWord == [x for x in roundWord]:
            wordnotSolved = False
    # Print roundstatus with string.format, tell people the state of the round as you are leaving a round.
    print(f'End of round {roundNum} status: {players}')

def main():
    #gameSetup()    
    global roundNum
    for i in range(0,2):
        if i in [0,1]:
            roundNum = i+1
            wofRound()
        else:
            return#wofFinalRound() -> final round to dos

if __name__ == "__main__":
    main()
    
