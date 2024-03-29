'''
Author:Anthony Pacheco
Class: CIS 129 
Date: 03/29/2024
Version: 5
Discription: This program will ask the user for playerOne/playerTwo custome names to be enter and
play a random dice game and the player that has a the hightest number will win and
then ask the user if they want to play again. 
'''

import random
def main():
    # This main will play a dice game with 2 player that can custmize their names

    print('Welcome to the Dice Game!')

    
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    

    while endProgram == 'no':
    #This while loop will let the games repeat as many time as the user wants 
        p1number = 0
        p2number = 0
        winnerName = 'NO NAME'
        
        p1number, p2number = rollDice(playerOne, playerTwo)

        winnerName = displayInfo(playerOne, playerTwo, p1number, p2number, winnerName)
    
        endProgram = runProgramAgain()
        
        

def inputNames(playerOne, playerTwo):
    # Getting Player Names
    print('Enter name for Player 1:')
    playerOne= input()
    print('Enter name for Player 2:')
    playerTwo = input()
    return playerOne, playerTwo


def rollDice(playerOne, playerTwo):
    # Rolling a 6 headed dice useing random.randint()
    p1number = random.randint(1,6)

    p2number = random.randint(1,6)
    
    return p1number, p2number
    
def displayInfo(playerOne, playerTwo, p1number, p2number, winnerName):
    # Desiding winner and displaying results 
    if p1number > p2number:
        winnerName = playerOne
    elif p1number < p2number:
        winnerName = playerTwo
    else:
        winnerName = 'Tie'
        
    print(playerOne, 'rolled', p1number)
    print(playerTwo, 'rolled', p2number)
    print('The winner is:', winnerName)
    return

def runProgramAgain():
    # This validate user input for yes or no to run game again
    print('Do you want to end program? (yes/no): ')
    endProgram = input()
    while endProgram.lower() != 'no' and endProgram.lower() != 'yes':
        print('Error, please enter (yes or no)!')
        print('Do you want to end program? (yes/no): ')
        endProgram = input()
        
    return endProgram.lower()

main()




















