#########################################
# Name: Ben Sadeh
# Date: Friday October 15
# Description: Hangman countries game
#########################################

#Store the secretWord into a variable
#Set usedLetters to an empty string
import random
words=["canada","america","russia","china", "japan", "brazil", "france", "england"]
secretWord=random.choice(words)
usedLetters=""
print('Welcome to hangman. A random country has been generated as your word you must guess. To guess a letter, follow the instructions on the screen. Press a letter key on the keyboard then press enter. You have 7 wromg guesses before the game will end. Good luck!')

#Set allowed attempts to 7
#Set guessed to False
attempts=int(7)
guessed=False

#Start a loop while attempts are more than zero and you did not guessed the word
while attempts>0 and guessed==False:
    missingLetters=len(secretWord)

#Start a for loop going though each letter from the secretWord
    for i in secretWord:
        if i in usedLetters:

#If yes - print the current letter (keep printing on the same lineuse comma)
#If not – print underscore " _ " (keep printing on the same line)
            print(i,end="")
            missingLetters-=1
        else:
            print(" _ ",end="")
    print(' Used Letters:', usedLetters)

#If the secretWord is guessed (no letters are missing), Print "You won!" message and exit the loop (change the Boolean variable)
#If not - Prompt user for an input  a new letter and store it in a variable newLetter
    if  missingLetters==0:
        print('You won!')
        guessed=True
    else:
        newLetter=input('Guess a letter: ')
        newLetter=newLetter.lower()

#Error proof the input - check for 1 letter input at a time use len() and
#check for a letter input (use a String method)
#check if the letter is not already guessed (inside the usedLetters string)
    if newLetter not in secretWord and newLetter not in usedLetters and len(newLetter)==1:
        attempts-=1
        print('Nope. You have '+str(attempts)+' attempts left.')

    if len(newLetter)==1 and newLetter.isalpha()==True and newLetter not in usedLetters:
        usedLetters+=newLetter
    elif missingLetters!=0 or len(newLetter)>1:
            print('Invalid imput. Try again')

#If no more attempts are allowed and you still did not guessed the word; Print a message and the secretWord
if attempts==0 and guessed==False:
    print('Oops, you have used up all your guesses. Game over!')
    print('The secret word is:', secretWord)
print('GAME OVER')
