'''Cootie Catcher Program that take user input to give them a function.
Built using Python 3.5 on Windows 10
Runs on any system with python 2 or 3'''

#add python2 support
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

import os
import random
from colorama import Fore, Style

#add linux/mac support
import sys
if sys.platform.startswith('win'):
    CLEAR_COMMAND = 'cls'
else:
    CLEAR_COMMAND = 'clear'

# read fortune constants.
with open('Fortunes.txt') as reader:
    F_FORTUNES = reader.readlines()    #Taking the fortunes out of the random document
with open('Yes_No.txt') as reader:
    YN_FORTUNES = reader.readlines()   #Taking the foutunes out of the yes_no document
with open('Trivia.txt') as reader:
    T_FORTUNES = reader.readlines()    #Taking the fortunes out of the trivia document

def intro():
    '''Header for the program, that will show up for the whole game'''
    print("--------------------------------")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|        Cootie Catcher        |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("--------------------------------")
    print("\n")

#yes this tiny function seems trivial but it is normal and pythonic
def choose_from_list(choice_list):
    """
    :param choice_list:
      a list of strings to choose from
    :return:
      a list of 8 random values from the choice_list, plus an empty string
    """
    return [random.choice(choice_list) for _ in range(8)] + [""]

def choose_from_user_input():
    """
    :return:
      a list of 8 user inputted strings, shuffled, plus an empty string
    """
    os.system(CLEAR_COMMAND)
    fortune = list()
    words = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'last']
    for word in words:
        #Word list to make sure the correct position is being referenced to the player
        intro()
        fortune.append(input("Enter your %s fortune: " % word))
        #Adding the individual fortunes
        os.system(CLEAR_COMMAND)
    random.shuffle(fortune)  #Finalizing the fortune list for the custom fortunes
    fortune.append("")

def choose_fortune(choose):
    '''
      There are four different fortune types that can be accessed
      This allows the choice between Random, Trivia, Yes_No Question or Custom)
      :param choose:
        string from the user indicating the catagory
      :return:
        a list of 8 strings plus a optional question.
    '''
    if choose.lower() == "choose":
        fortune = choose_from_user_input()
    if choose.lower() == "random":
        fortune = choose_from_list(F_FORTUNES)
    if choose.lower() == "trivia":
        fortune = choose_from_list(T_FORTUNES)
    if choose.lower() == "question":
        fortune = choose_from_list(YN_FORTUNES)
        question = input("\nWhat is your question? ").strip()
        #Adding the asked question to the fortunes list, so it can be called back later
        fortune[-1] = question #replace the last value
    return fortune

#this may be a little confusing to you. We make a function that makes a function.
#(This is called a lambda or closure in CS)
#See how this means if we want to remove Style.BRIGHT or something, there is
#a single place in the code that needs to be modified
def make_color_func(color):
    """makes a closure to return a colored string
    :param color:
      ANSI color string
    :return:
      function that sets an argument to that color
    """
    def color_func(arg):
        return color + Style.BRIGHT + arg + Style.RESET_ALL
    return color_func

#these are equivalent to def statements
red = make_color_func(Fore.RED)
blue = make_color_func(Fore.BLUE)
green = make_color_func(Fore.GREEN)
yellow = make_color_func(Fore.YELLOW)

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

def user_choice(choice_list, question=">", prompt=None):
    """
    presents the user with a list of choices and asks them to pick one
    :param choice_list:
      list of strings to choose from; must all be lowercase
    :param question:
      string to be asked in the input call
    :param prompt:
      optional additional string to be printed before the input call
    :return:
      the users choice, lowercase, stripped of whitespace
    """
    if prompt:
        print(prompt)
    choice = input(question).strip()
    while choice not in choice_list:
        print("\nInvalid Choice\n")
        if prompt:
            print(prompt)
        choice = input(question).strip()
    return choice

def user_choice_num(choice_list):
    """
    presents the user with a list of numbers and asks them to pick one
    """
    question = "Choose {}: ".format(", ".join(choice_list))
    return user_choice(choice_list, question)

def num(color, number):
    '''
        Function to determine what numbers will be displayed next
        Color = Chosen Color, num = Number picked on first time
        If num == 0, this is the first time a number has been chosen
        Used color length because it is easier to just deal with even and odd
    '''
    if len(color) % 2 == 0 and number == 0:
        choose_num = user_choice_num(['1', '4', '5', '8'])
    elif number % 2 == 0 and len(color) % 2 == 0 or number % 2 == 1 and len(color) % 2 == 1:
        choose_num = user_choice_num(['1', '4', '5', '8'])
    elif len(color) % 2 == 1 and number == 0:
        choose_num = user_choice_num(['2', '3', '6', '7'])
    elif number % 2 == 1 and len(color) % 2 == 0 or number % 2 == 0 and len(color) % 2 == 1:
        choose_num = user_choice_num(['2', '3', '6', '7'])
    #WARNING: you have no else case! are you sure all bases are covered?
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

def change_fortune():
    os.system(CLEAR_COMMAND)
    intro()
    prompt = "Would you like to Choose your own fortunes / Get Random ones / Get Trivia facts / Ask specific Question? \n"
    question = "Enter Choose, Random, Trivia or Question: "
    choice_list = ['choose', 'random', 'trivia', 'question']
    fortune_choice = user_choice(choice_list, question, prompt)

    # Creates the fortunes based on fortune type
    fortune = choose_fortune(fortune_choice)
    return fortune

def play(fortune):
    """play a single round"""
    os.system(CLEAR_COMMAND)
    intro()
    print_question(fortune)  #If a question was asked, it will be printed here

    #Asking the player to pick a color
    question = "Choose %s, %s, %s or %s: " %(red('Red'), blue('Blue'), green('Green'), yellow('Yellow'))
    color = user_choice(['yellow', 'blue', 'green', 'red'], question)

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

def cootie():
    '''Main function that puts everything together'''
    fortune = change_fortune()
    while True:  #Loop makes sure the game keeps going until the player tells it to stop
        play(fortune)

        #Choice of if player wants to keep playing
        again = user_choice(['y', 'n'], "Would you like to play again? Y or N:")
        if again == 'n': #If the player chooses no the loop breaks
            break

        #Choice of if the player wants new fortunes
        change = user_choice(['y', 'n'], "Would you like to change your fortunes or question? Y or N? ")
        if change == 'y':  #Gives the player the option to pick a different fortune type
            fortune = change_fortune()

if __name__ == "__main__":
    cootie()  #Running the code
