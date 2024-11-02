header = """
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Dominik Šváb
email: dominik.svab123@gmail.com
"""
import random
import time

separator = 47 * "-"
hi_message = "Hi, there!"
game_info_message_1 = "I've generated a random 4-digit number for you."
game_info_message_2 = "Let's play a bulls and cows game!"
game_info_message_3 = "Enter a number:"

def print_game_intro():
    print(separator)
    print(hi_message)
    print(separator)
    
def generate_random_number():
    number_no_0 = list("123456789")
    numbers = list("0123456789")

    random_number = random.choice(number_no_0)
    numbers.remove(random_number)

    for a in range(3):
        digit = random.choice(numbers)
        random_number += digit
        numbers.remove(digit)
    return random_number

def print_game_info():
    print(game_info_message_1)
    print(game_info_message_2)
    print(separator)
    print(game_info_message_3)
    print(separator)


def is_valid_entry(number_entry):
    return (
        number_entry.isdigit() and 
        len(set(number_entry)) == 4 and 
        number_entry[0] != "0" and
        len(number_entry) == 4
    )

def handle_invalid_entry(number_entry):
    if len(number_entry) != 4:
        print("You must enter a 4-digit number!")
    elif not number_entry.isdigit():
        print("The input must contain only digits!")
    elif number_entry[0] == "0":
        print("The number cannot start with a 0!")
    elif len(set(number_entry)) != 4:
        print("All digits in the number must be unique!")


def count_bulls_and_cows(number_entry, random_number):
    cows = 0
    bulls = 0

    for i in range(4):
        if number_entry[i] == random_number[i]:
            bulls += 1
        elif number_entry[i] in random_number:
            cows += 1
    return bulls, cows

def print_bulls_and_cows(bulls, cows):
    if bulls == 1 and cows == 1:
        print("1 bull, 1 cow")
    elif bulls != 1 and cows == 1:
        print(bulls, "bulls, 1 cow")
    elif bulls == 1 and cows != 1:
        print("1 bull,", cows, "cows")
    else:
        print(bulls, "bulls,", cows, "cows")

def end_game(guess_count, start_time):
    end_time = time.time()
    elapsed_time = round(end_time - start_time)

    if guess_count > 1:
        print("Correct, you've guessed the right number \nin", guess_count, "guesses!")
        print("Time spent playing:", elapsed_time,"seconds.")
        
    else:
        print("You are very lucky! You've guessed the right \nnumber in first guess!")
        print("Time spent playing:", elapsed_time,"seconds.")
   
    print(separator)
    print("That's amazing!")

def play_game(random_number):
    number_entry = input(">>> ")
    start_time = time.time()
    guess_count = 1

    while number_entry != random_number:
        if is_valid_entry(number_entry):
            guess_count += 1
            bulls, cows = count_bulls_and_cows(number_entry, random_number)
            print_bulls_and_cows(bulls, cows)

        elif number_entry == "cancel":
            print("Ending the game, the number was", random_number)
            print(separator)
            break

        else:
            handle_invalid_entry(number_entry)
        
        print(separator)
        number_entry = input(">>> ")
    else:
        end_game(guess_count, start_time)


print(header)
print_game_intro()
random_number = generate_random_number()
print_game_info()
play_game(random_number)



    
