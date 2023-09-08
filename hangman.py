#ALL words imported from project Moby Word II (https://www.gutenberg.org/files/3201/files/)
#Some modifications were made to the file for this specific program
#Please download the COMMON.txt file along with the program for it to run without issues
#Ensure they are in the same directory

import random

#<-- ASCII ART SECTION -->
hangman_title = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ 
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#<-- MAIN PROGRAM -->

print(hangman_title)

# opening the file in read mode
my_file = open("COMMON.txt", "r") 
# reading the file
data = my_file.read()
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")

#Choosing a random word
ran_index = -1

#assigning ran_index with a random index from the list
ran_index = random.randint(0, len(data_into_list))

#Selecting the word at that index from the list
ran_word = data_into_list[ran_index]

#Since the text file is from a 3rd party source, avoid header words that are commonly found in dictionaries
#ex. ab. which indicates words starting from ab
if ran_word[len(ran_word) - 1] == '.' or len(ran_word) < 2:
    while(ran_word[len(ran_word) - 1] == '.') or len(ran_word) < 2:
        ran_index = random.randint(0, len(data_into_list))
        ran_word = data_into_list[ran_index]

#Close the file since the word has been chosen
my_file.close()

#After word has been chosen
#Print the blank spaces only for letters, symbols are printed as they are
#Only show it for the first time

#Storing the letters that the user inputs to cross-check against the word
word_check = ""

print(ran_word)
for i in range(0, len(ran_word)):
    if(ran_word[i].isalpha()):
        print("_ ", end = " ")
        word_check += "_"
    else:
        print(ran_word[i], end = " ")
        word_check += ran_word[i]
print()

#To check if the max number of mistakes have been reached
mistakes_count = 0

#To check if the user has guessed the word
correct_flag = False

#To print the ASCII art
stages_count = -1

while mistakes_count < 6 and not correct_flag:
    letter = input("Enter your guess: ")
    
    #Check if the user input is in the randomly generated word
    if letter in ran_word:
        print("Correct guess!")

        #Wherever the letter is found, replace the blank (_) with the letter
        for i in range(len(ran_word)):
            if ran_word[i] == letter:
                word_check = word_check[:i] + letter + word_check[i + 1:]
        print(word_check)
        print(stages[stages_count])

        #If user guesses the entire word correctly, then they automatically win
        if word_check == ran_word or letter == ran_word:
            print("Congratulations, you win!")
            correct_flag = True

    else:
        #If wrong guess then increment the msitakes
        mistakes_count += 1
        if mistakes_count < 6:
            print("Wrong guess! Try again")
            stages_count -= 1
            print(stages[stages_count])
        else:
            stages_count -= 1
            print(stages[stages_count])
            print("You have used up all your chances. Game Over!")

if not correct_flag:
    print(f"The word was '{ran_word}'. Better luck next time!")

#<-- END OF PROGRAM -->