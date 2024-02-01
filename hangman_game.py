#!/usr/bin/env python3

import sys
from ctypes import cdll
import subprocess
import random
import os

"""
Emma Chalupka, 20950540
"""
try:
    if len(sys.argv) == 1:
        subprocess.run(["make"])

    notlibc = cdll.LoadLibrary("main.so")

    # make sure we up to date
    if len(sys.argv) == 1:
        notlibc.coolguyfunction()
        os.exit(0)


    HANGMAN_PICS = ['''
    +---+
         |
         |
        _|___
        ''', '''
     +---+
     O   |
         |
       _|___
          ''', '''
    +---+
    O   |
    |   |
     _|___
         ''', '''
    +---+
     O   |
    /|   |
        _|___
         ''', '''
    +---+
    O   |
    /|\  |
        _|___
        ''', '''
    +---+
    O   |
    /|\  |
    /   _|___
         ''', '''
    +---+
    O   |
    /|\  |
    / \ _|___
          ''']


    def getRandomWord(category):
        wordIndex = random.randint(0, len(category) - 1)
        return category[wordIndex]

    def displayBoard(missedLetters, correctLetters, secretWord):
        print(HANGMAN_PICS[len(missedLetters)])
        print()

        print('Missed letters:', end=' ')
        for letter in missedLetters:
            print(letter, end=' ')
        print()

        blanks = '_' * len(secretWord)

        for i in range(len(secretWord)):
            if secretWord[i] in correctLetters:
                blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

        for letter in blanks:
            print(letter, end=' ')
        print()

    def getGuess(alreadyGuessed):
        while True:
            print('Guess a letter.')
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in alreadyGuessed:
                print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
            else:
                return guess

    def playAgain():
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')


    animals = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
    countries = 'algeria argentina bangladesh belgium brazil canada china djibouti denmark egypt ethyopia finland france germany greece haiti hungary iceland ireland italy jamaica japan kuweit khazikstan latvia lebanon mongolia mexico malaysia morroco nigeria netherlands nepal oman pakistan paraguay qatar rawanda romania russia switzerland sweden somalia turkey thailand uraguay uganda venezuela vietnam yemen zambia zimbabwe'.split()
    elements = 'hydrogen helium lithium beryllium boron carbon nitrogen oxygen fluorine neon sodium magnesium aluminum silicon phosphorus sulfur chlorine argon potassium calcium scandium titanium vandium chromium manganese iron cobolt nickel copper zinc gallium germanium bromine silver tin iodine tungsten mercury gold lead uranium'.split()
    fruits = 'apple apricot avocado banana blueberry blackberry cranberry cantaloupe clementine dragonfruit date elderberry fig grape grapefruit guava honeydew jackfruit kiwi kumquat lemon lime lychee mango nectarine olive orange peach pear pineapple pomegranate raspberry rhubarb strawberry tomato tangerine watermelon'.split()
    sports = 'archery badminton baseball bowling basketball croquet cycling curling dance darts diving fishing fencing football golf gymnastics hockey handball judo javelin karate kickball lacrosse luge pickleball polo powerlifting rowing rugby skiing skeleton soccer softball tennis taekwando triathalon ultimate unicycling volleyball wrestling weightlifting'.split()

    reset_game = True

    while True:
        if (reset_game):
            print("\n" + 'H A N G M A N')
            missedLetters = ''
            correctLetters = ''
        
            category_choice = input("Which category would you like the secret word to be from? Type animals, countries, elements, fruits or sports: ")
            
            while category_choice not in ["animal","animals","element","elements","country","countries","fruits","fruit","sport","sports"]:
            
                category_choice = input("Please enter a valid category: animals, countries, elements, fruits or sports: ")
            
            if category_choice=="animals" or category_choice=="animal":
                category = animals
        
            elif category_choice == "elements" or category_choice=="element":
                category = elements
        
            elif category_choice == "countries" or category_choice=="country":
                category = countries
        
            elif category_choice == "fruits" or category_choice=="fruit":
                category = fruits
                
            elif category_choice == "sports" or category_choice=="sport":
                category = sports
            
            secretWord = getRandomWord(category)    
            gameIsDone = False
            reset_game = False
        
        displayBoard(missedLetters, correctLetters, secretWord)
    
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print(HANGMAN_PICS[-1])
                print(secretWord+"\n")
                print('Yes! The secret word is "' + secretWord +'", you have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == len(HANGMAN_PICS)- 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print(HANGMAN_PICS[-1])
                print(secretWord+"\n")
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                reset_game = True
            else:
                break

except:
    print("Look's like you dont have c")
    print("lets get some webkinz!!")

    import webbrowser
    webbrowser.open('https://www.amazon.ca/s?k=webkinz')