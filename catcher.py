#Built using Python 3.5 on Windows 10

import os
import random
import colorama 
from colorama import Fore, Style

#Header for the program, that will show up for the whole game
def intro():
  print ("--------------------------------")
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("|        Cootie Catcher        |")
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("--------------------------------")
  print ("\n")

def open_docs(): #Opening the fortune documents and putting them into lists
  with open('Fortunes.txt') as f:
    f_fortunes = f.readlines()    #Taking the fortunes out of the random document
  with open('Yes_No.txt') as f:
    yn_fortunes = f.readlines()   #Taking the foutunes out of the yes_no document
  with open('Trivia.txt') as f:
    t_fortunes = f.readlines()    #Taking the fortunes out of the trivia document
  return (f_fortunes, yn_fortunes, t_fortunes)

#There are four different fortune types that can be accessed
#This allows the choice between Random, Trivia, Yes_No Question or Custom)
def choose_fortune(choose,f_fortunes, yn_fortunes, t_fortunes): 
  fortune = list()
  if choose.lower() == "choose":
    os.system('cls')
    for x in range(0,8):
      word = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'last' ]
      #Word list to make sure the correct position is being referenced to the player
      intro()
      fortune.insert(x, '"' + input("Enter your %s fortune: " % word[x]).strip() + '"' )
      #Adding the individual fortunes
      os.system('cls')  
    random.shuffle(fortune)  #Finalizing the fortune list for the custom fortunes
    fortune.append("")
  if choose.lower() == "random":
    for x in range(0, 8):
      fortune.insert(x, random.choice(f_fortunes)) #Creating the fortune list for the random fortunes
    fortune.append("")
  if choose.lower() == "trivia":
    for x in range(0, 8):
      fortune.insert(x, random.choice(t_fortunes)) #Creating the fortune list for the trivia fortunes
    fortune.append("")                                          
  if choose.lower() == "question":
    for x in range(0, 8):
      fortune.insert(x, random.choice(yn_fortunes))  #Creating the fortune list for the yes_no fortunes
    question = input("\nWhat is your question? ").strip()
    fortune.append(question) #Adding the asked question to the fortunes list, so it can be called back later
  return fortune  

def red(arg):  # Function used for turning specified strings BRIGHT RED
  response = (Fore.RED + Style.BRIGHT + arg + Style.RESET_ALL)
  return response

def blue(arg):  # Function used for turning specified strings BRIGHT BLUE
  response = (Fore.BLUE + Style.BRIGHT + arg  + Style.RESET_ALL)
  return response

def green(arg):  # Function used for turning specified strings BRIGHT GREEN
  response = (Fore.GREEN + Style.BRIGHT + arg  + Style.RESET_ALL)
  return response

def yellow(arg):  # Function used for turning specified strings BRIGHT YELLOW
  response = (Fore.YELLOW + Style.BRIGHT + arg  + Style.RESET_ALL)
  return response
	  
def string_moves(color): #Counts out the Cootie Catcher's moves for the specified color
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

#Function to determine what numbers will be displayed next
#Color = Chosen Color, num = Number picked on first time
#If num == 0, this is the first time a number has been chosen
#Used color length because it is easier to just deal with even and odd
def num(color, num):
  if len(color) % 2 == 0 and num == 0 or num % 2 == 0 and len(color) % 2 == 0  or num % 2 == 1 and len(color) % 2 == 1:
    num = str(input("Choose 1, 4, 5, 8: ")).strip()
    while num not in ['1', '4', '5', '8']:
      print("\nInvalid Choice\n")
      num = str(input("Choose 1, 4, 5, 8: ")).strip()
  elif len(color) % 2 == 1 and num == 0 or num % 2 == 1 and len(color) % 2 == 0 or num % 2 == 0 and len(color) % 2 == 1:  
    num = str(input("Choose 2, 3, 6, 7: ")).strip()
    while num not in ['2', '3', '6', '7']:
      print("\nInvalid Choice\n")
      num = str(input("Choose 2, 3, 6, 7: ")).strip() 
  numint = int(num)
  return numint

def int_moves (arg,color): #Counts out the Cootie Catcher's moves for the specified number
  response = ''  #Initializes the response variable
  for index in range(1, arg+1):
    response += str(index) + ".... " #Adds to the response variable based on the specified number
  if color =='red':
    response = red(response) #Turns response red
  elif color =='blue':
    response = blue(response) #Turns response blue
  elif color =='green':
    response = green(response) #Turns response green
  else:
    response = yellow(response) #Turns response yellow
  respond = "\nCootie Catcher Responds: "  #Creating a different variable for the response without the color change 
  return (respond + response + '\n')  #Combines respond and response to give final response

#If a question was asked it was saved at the end of the fortune list
#This function calls that value from the list
def print_question (list):
  if list[8]:
    print("Question: " + list[8] + '\n')
	
#This function prints the specific fortune that the player landed on
def fortune_print(arg, list):
  print(list[arg-1])
  print('\n')

def cootie():
  intro()
  again = 'y' #Initializing that the player wants to play the first time
  change = 'y' #Initializing the the player wants to choose their first fortune type
  while again == 'y':  #Loop makes sure the game keeps going until the player tells it to stop
    if change == 'y':  #Gives the player the option to pick a different fortune type
      f_fortunes, yn_fortunes, t_fortunes =   open_docs() #Opens the fortune documents and populate fortune lists
      print("Would you like to Choose your own fortunes / Get Random ones / Ask specific Question? \n")
      fortune_choice = input("Enter Choose, Random, Trivia or Question: ")
      fortune = choose_fortune(fortune_choice,f_fortunes, yn_fortunes, t_fortunes) #Creates the fortunes based on fortune type
      while fortune_choice.lower() not in ['choose', 'random', 'trivia', 'question']:
        print("\nInvalid Choice\n")
        print("Would you like to Choose your own fortunes / Get Random ones / Ask specific Question? \n")
        fortune_choice = input("Enter Choose, Random, Trivia or Question: ").strip()

    os.system('cls')
    intro()
    print_question(fortune)  #If a question was asked, it will be printed here
    #Asking the player to pick a color
    color = input("Choose %s, %s, %s or %s: " % (red('Red'), blue('Blue'), green('Green'), yellow('Yellow'))).strip()
    while color.lower() not in ['yellow', 'blue', 'green', 'red']:
      print("\nInvalid Choice\n")
      color = input("Choose %s, %s, %s or %s: " % (red('Red'), blue('Blue'), green('Green'), yellow('Yellow'))).strip()
    string_move = string_moves(color.lower()) #Showing how the catcher 'moves'
    print(string_move)
    numint = num(color,0) #Asking the player to pick a number
    int_move = int_moves(numint,color.lower()) #Showing how the catcher 'moves'
    print(int_move)
    num2int = num(color, numint) #Asking the player to pick another number
    int2_move = int_moves(num2int,color.lower()) #Showing how the catcher 'moves'
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

  
  





















