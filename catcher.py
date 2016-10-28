'''Cootie Catcher Program that take user input to give them a function.
Built using Python 3.5 on Windows 10'''

import os
import random
from colorama import Fore, Style

def intro():
    '''Header for the program, that will show up for the whole game'''
    print("--------------------------------")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|        Cootie Catcher        |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("--------------------------------")
    print("\n")

def open_docs():
    '''
       Opening the fortune documents and putting them into lists
    '''
    with open('Fortunes.txt') as reader:
        f_fortunes = reader.readlines()    #Taking the fortunes out of the random document
    with open('Yes_No.txt') as reader:
        yn_fortunes = reader.readlines()   #Taking the foutunes out of the yes_no document
    with open('Trivia.txt') as reader:
        t_fortunes = reader.readlines()    #Taking the fortunes out of the trivia document
    return(f_fortunes, yn_fortunes, t_fortunes)

def choose_fortune(choose, f_fortunes, yn_fortunes, t_fortunes):
    '''
      There are four different fortune types that can be accessed
      This allows the choice between Random, Trivia, Yes_No Question or Custom)
    '''
    fortune = list()
    if choose.lower() == "choose":
        os.system('cls')
        for counter in range(0, 8):
            word = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'last']
            #Word list to make sure the correct position is being referenced to the player
            intro()
            fortune.insert(counter, '"' + input("Enter your %s fortune: " % word[counter]).strip() + '"')
            #Adding the individual fortunes
            os.system('cls')
        random.shuffle(fortune)  #Finalizing the fortune list for the custom fortunes
        fortune.append("")
    if choose.lower() == "random":
        for counter in range(0, 8):
            #Creating the fortune list for the random fortunes
            fortune.insert(counter, random.choice(f_fortunes))
        fortune.append("")
    if choose.lower() == "trivia":
        for counter in range(0, 8):
            #Creating the fortune list for the trivia fortunes
            fortune.insert(counter, random.choice(t_fortunes))
        fortune.append("")
    if choose.lower() == "question":
        for counter in range(0, 8):
            #Creating the fortune list for the yes_no fortunes
            fortune.insert(counter, random.choice(yn_fortunes))
        question = input("\nWhat is your question? ").strip()
        #Adding the asked question to the fortunes list, so it can be called back later
        fortune.append(question)
    return fortune

def red(arg):
    ''' Function used for turning specified strings BRIGHT RED '''
    response = (Fore.RED + Style.BRIGHT + arg + Style.RESET_ALL)
    return response

def blue(arg):
    ''' Function used for turning specified strings BRIGHT BLUE '''
    response = (Fore.BLUE + Style.BRIGHT + arg  + Style.RESET_ALL)
    return response

def green(arg):
    ''' Function used for turning specified strings BRIGHT GREEN '''
    response = (Fore.GREEN + Style.BRIGHT + arg  + Style.RESET_ALL)
    return response

def yellow(arg):
    ''' Function used for turning specified strings BRIGHT YELLOW '''
    response = (Fore.YELLOW + Style.BRIGHT + arg  + Style.RESET_ALL)
    return response

def string_moves(color):
    '''
        Counts out the Cootie Catcher's moves for the specified color
    '''
    response = '\nCootie Catcher Responds: '
    if color == 'red':
        response += red('R...E...D...') + '\n' #Turns response red
    elif color == 'blue':
        response += blue('B...L...U...E...') +'\n' #Turns response blue
    elif color == 'green':
        response += green('G...R...E...E...N...') + '\n' #Turns response green
    else:
        response += yellow('Y...E...L...L...O...W...') +'\n' #Turns response yellow
    return response

def num(color, number):
    '''
        Function to determine what numbers will be displayed next
        Color = Chosen Color, num = Number picked on first time
        If num == 0, this is the first time a number has been chosen
        Used color length because it is easier to just deal with even and odd
    '''
    if len(color) % 2 == 0 and number == 0:
        choose_num = str(input("Choose 1, 4, 5, 8: ")).strip()
        while choose_num not in ['1', '4', '5', '8']:
            print("\nInvalid Choice\n")
            choose_num = str(input("Choose 1, 4, 5, 8: ")).strip()
    elif number % 2 == 0 and len(color) % 2 == 0 or number % 2 == 1 and len(color) % 2 == 1:
        choose_num = str(input("Choose 1, 4, 5, 8: ")).strip()
        while choose_num not in ['1', '4', '5', '8']:
            print("\nInvalid Choice\n")
            choose_num = str(input("Choose 1, 4, 5, 8: ")).strip()
    elif len(color) % 2 == 1 and number == 0:
        choose_num = str(input("Choose 2, 3, 6, 7: ")).strip()
        while choose_num not in ['2', '3', '6', '7']:
            print("\nInvalid Choice\n")
            choose_num = str(input("Choose 2, 3, 6, 7: ")).strip()
    elif number % 2 == 1 and len(color) % 2 == 0 or number % 2 == 0 and len(color) % 2 == 1:
        choose_num = str(input("Choose 2, 3, 6, 7: ")).strip()
        while choose_num not in ['2', '3', '6', '7']:
            print("\nInvalid Choice\n")
            choose_num = str(input("Choose 2, 3, 6, 7: ")).strip()
    numint = int(choose_num)
    return numint

def int_moves(arg, color):
    '''
        Counts out the Cootie Catcher's moves for the specified number
    '''
    response = ''  #Initializes the response variable
    for index in range(1, arg+1):
        #Adds to the response variable based on the specified number
        response += str(index) + ".... "
    if color == 'red':
        response = red(response) #Turns response red
    elif color == 'blue':
        response = blue(response) #Turns response blue
    elif color == 'green':
        response = green(response) #Turns response green
    else:
        response = yellow(response) #Turns response yellow
    #Creating a different variable for the response without the color change
    respond = "\nCootie Catcher Responds: "
    #Combines respond and response to give final response
    return respond + response + '\n'

def print_question(fortune):
    '''
        If a question was asked it was saved at the end of the fortune list
        This function calls that value from the list
    '''
    if fortune[8]:
        print("Question: " + fortune[8] + '\n')

def fortune_print(arg, fortune):
    ''' This function prints the specific fortune that the player landed on '''
    print(fortune[arg-1])
    print('\n')

def cootie():
    '''Main function that puts everything together'''
    intro()
    again = 'y' #Initializing that the player wants to play the first time
    change = 'y' #Initializing the the player wants to choose their first fortune type
    while again == 'y':  #Loop makes sure the game keeps going until the player tells it to stop
        if change == 'y':  #Gives the player the option to pick a different fortune type
            #Opens the fortune documents and populate fortune lists
            f_fortunes, yn_fortunes, t_fortunes = open_docs()
            print("Would you like to Choose your own fortunes / Get Random ones / Get Trivia facts / Ask specific Question? \n")
            fortune_choice = input("Enter Choose, Random, Trivia or Question: ")
            # Creates the fortunes based on fortune type
            fortune = choose_fortune(fortune_choice, f_fortunes, yn_fortunes, t_fortunes)
            while fortune_choice.lower() not in ['choose', 'random', 'trivia', 'question']:
                print("\nInvalid Choice\n")
                print("Would you like to Choose your own fortunes / Get Random ones / Get Trivia facts / Ask specific Question? \n")
                fortune_choice = input("Enter Choose, Random, Trivia or Question: ").strip()

        os.system('cls')
        intro()
        print_question(fortune)  #If a question was asked, it will be printed here
    #Asking the player to pick a color
        color = input("Choose %s, %s, %s or %s: " %(red('Red'), blue('Blue'), green('Green'), yellow('Yellow'))).strip()
        while color.lower() not in ['yellow', 'blue', 'green', 'red']:
            print("\nInvalid Choice\n")
            color = input("Choose %s, %s, %s or %s: " %(red('Red'), blue('Blue'), green('Green'), yellow('Yellow'))).strip()
        string_move = string_moves(color.lower()) #Showing how the catcher 'moves'
        print(string_move)
        numint = num(color, 0) #Asking the player to pick a number
        int_move = int_moves(numint, color.lower()) #Showing how the catcher 'moves'
        print(int_move)
        num2int = num(color, numint) #Asking the player to pick another number
        int2_move = int_moves(num2int, color.lower()) #Showing how the catcher 'moves'
        print(int2_move)
        print_question(fortune) #If a question was asked, it will be printed again
        fortune_print(num2int, fortune)
    #Choice of if player wants to keep playing
        again = input("Would you like to play again? Y or N: ").lower().strip()
        while again not in ['y', 'n']:
            print("\nInvalid Choice\n")
            again = input("Would you like to play again? Y or N: ").lower().strip()
        if again == 'n': #If the player chooses no the loop breaks
            break
    #Choice of if the player wants new fortunes
        change = input("Would you like to change your fortunes or question? Y or N? ").lower().strip()
        while change not in ['y', 'n']:
            print("\nInvalid Choice\n")
            change = input("Would you like to change your fortunes or question? Y or N? ").lower().strip()
        os.system('cls')
        intro()

os.system('cls')
cootie()  #Running the code
