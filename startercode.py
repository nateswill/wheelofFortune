from config import dictionaryloc
from config import turntextloc
from config import wheeltextloc
from config import maxrounds
from config import vowelcost
from config import roundstatusloc
from config import finalprize
from config import finalRoundTextLoc

import random

players={0:{"roundtotal":0,"gametotal":0,"name":"Bad Bunny"},
         1:{"roundtotal":0,"gametotal":0,"name":"Karol G"},
         2:{"roundtotal":0,"gametotal":0,"name":"Lizzo"},
        }


roundNum = 0 # number for rounds 1,2,3
dictionary = ['mississippi', 'erroneous', 'teradactyl', 'symphony', 'orchestra'] # list of words to select at random
turntext = "" # 
wheelList = ['BANKRUPT', 'LOSE A TURN', 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
roundWord = ""
blankWord = []
vowels = {"a", "e", "i", "o", "u"}
roundStatus = ""
finalRoundText = ""


def readDictionaryFile():
    global dictionary
    # Read dictionary file in from dictionary file location
    # Store each word in a list.
      
    
def readTurnTxtFile():
    global turntext   
    #read in turn intial turn status "message" from file

        
def readFinalRoundTxtFile():
    global finalroundtext   
    #read in turn intial turn status "message" from file

def readRoundStatusTxtFile():
    global roundstatus
    # read the round status  the Config roundstatusloc file location 

def readWheelTxtFile():
    global wheellist
    # read the Wheel name from input using the Config wheelloc file location 
    
def getPlayerInfo():
    global players
    # read in player names from command prompt input


def gameSetup():
    # Read in File dictionary
    # Read in Turn Text Files
    global turntext
    global dictionary
        
    readDictionaryFile()
    readTurnTxtFile()
    readWheelTxtFile()
    getPlayerInfo()
    readRoundStatusTxtFile()
    readFinalRoundTxtFile() 
    
def getWord():
    global dictionary
    #choose random word from dictionary
    roundWord = random.choice(dictionary).upper()
    #make a list of the word with underscores instead of letters.
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
    initPlayer = random.choice([1,2,3])
    # Use getWord function to retrieve the word and the underscore word (blankWord)
    roundWord, blankWord = getWord()
    return initPlayer


def spinWheel(playerNum):
    global wheellist
    global players
    global vowels

    # Get random value for wheellist
    # Check for bankrupcy, and take action.
    # Check for loose turn
    # Get amount from wheel if not loose turn or bankruptcy
    # Ask user for letter guess
    # Use guessletter function to see if guess is in word, and return count of correct letter in word
    # Change player round total if they guess right.
    return stillinTurn


def guessLetter(letter, playerNum):
    global players
    global blankWord
    # parameters:  take in a letter guess and player number
    # Change position of found letter in blankWord to the letter instead of underscore 
    # return goodGuess= true if it was a correct guess
    # return count of letters in word. 
    # ensure letter is a consonate.
    
    return goodGuess, count

def buyVowel(playerNum):
    global players
    global vowels
    
    # Take in a player number
    # Ensure player has 250 for buying a vowelcost
    # Use guessLetter function to see if the letter is in the file
    # Ensure letter is a vowel
    # If letter is in the file let goodGuess = True
    
    return goodGuess      
        
def guessWord(playerNum):
    global players
    global blankWord
    global roundWord
    
    # Take in player number
    # Ask for input of the word and check if it is the same as wordguess
    # Fill in blankList with all letters, instead of underscores if correct
    # return False (to indicate the turn will finish)
    
    return False
    
    
def wofTurn(playerNum):  
    global roundWord
    global blankWord
    global turntext
    global players

    # take in a player number. 
    # use the string.format method to output your status for the round
    # and Ask to (s)pin the wheel, (b)uy vowel, or G(uess) the word using
    # Keep doing all turn activity for a player until they guess wrong
    # Do all turn related activity including update roundtotal 
    
    stillinTurn = True
    while stillinTurn:
        
        # use the string.format method to output your status for the round
        # Get user input S for spin, B for buy a vowel, G for guess the word
                
        if(choice.strip().upper() == "S"):
            stillinTurn = spinWheel(playerNum)
        elif(choice.strip().upper() == "B"):
            stillinTurn = buyVowel(playerNum)
        elif(choice.upper() == "G"):
            stillinTurn = guessWord(playerNum)
        else:
            print("Not a correct option")        
    
    # Check to see if the word is solved, and return false if it is,
    # Or otherwise break the while loop of the turn.     


def wofRound():
    global players
    global roundWord
    global blankWord
    global roundstatus
    initPlayer = wofRoundSetup()
    
    # Keep doing things in a round until the round is done ( word is solved)
        # While still in the round keep rotating through players
        # Use the wofTurn fuction to dive into each players turn until their turn is done.
    
    # Print roundstatus with string.format, tell people the state of the round as you are leaving a round.

def wofFinalRound():
    global roundWord
    global blankWord
    global finalroundtext
    winplayer = 0
    amount = 0
    
    # Find highest gametotal player.  They are playing.
    # Print out instructions for that player and who the player is.
    # Use the getWord function to reset the roundWord and the blankWord ( word with the underscores)
    # Use the guessletter function to check for {'R','S','T','L','N','E'}
    # Print out the current blankWord with whats in it after applying {'R','S','T','L','N','E'}
    # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
    # Print out the current blankWord again
    # Remember guessletter should fill in the letters with the positions in blankWord
    # Get user to guess word
    # If they do, add finalprize and gametotal and print out that the player won 


def main():
    gameSetup()    

    for i in range(0,2):
        if i in [0,1]:
            wofRound()
        else:
            wofFinalRound()

if __name__ == "__main__":
    main()
    
    
