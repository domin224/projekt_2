header = """
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Dominik Šváb
email: dominik.svab123@gmail.com
"""
separator = 47 * "-"
hi_message = "Hi, there!"
game_info_message_1 = "I've generated a random 4-digit number for you."
game_info_message_2 = "Let's play a bulls and cows game!"
game_info_message_3 = "Enter a number:"

print(header)
print(separator)
print(hi_message)
print(separator)

import random

number_no_0 = "123456789"
numbers = "0123456789"

result = random.choice(number_no_0)
numbers = numbers.replace(result, "")

for a in range(3):
    digit = random.choice(numbers)
    result += digit
    numbers = numbers.replace(digit, "")

print(game_info_message_1)
print(game_info_message_2)
print(separator)
print(game_info_message_3)
print(separator)

import time

number_entry = input(">>> ")
start_time = time.time()
guess_count = 1

while number_entry != result:
    
    if number_entry.isdigit() and len(set(number_entry)) == 4 and number_entry[0] != "0":
        
        guess_count += 1
        cows = 0
        bulls = 0

        for i in range(4):
            if number_entry[i] == result[i]:
                bulls += 1
            elif number_entry[i] in result:
                cows += 1
        
        if bulls == 1 and cows == 1:
            print("1 bull, 1 cow")
        elif bulls != 1 and cows == 1:
            print(bulls, "bulls, 1 cow")
        elif bulls == 1 and cows != 1:
            print("1 bull,", cows, "cows")
        else:
            print(bulls, "bulls,", cows, "cows")

    elif number_entry == "cancel":
        print("Ending the game, the number was", result)
        print(separator)
        break

    elif len(number_entry) != 4:
        print("You must enter a 4-digit number!")

    elif not number_entry.isdigit():
        print("The input must contain only digits!")

    elif number_entry[0] == "0":
        print("The number cannot start with a 0!")

    elif len(set(number_entry)) != 4:
        print("All digits in the number must be unique!")

    print(separator)
    number_entry = input(">>> ")
    
else:
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time = round(elapsed_time, 2)

    if guess_count > 1:
        print("Correct, you've guessed the right number \nin", guess_count, "guesses!")
        print("Time spent playing:", elapsed_time,"seconds.")
        print(separator)
        print("That's amazing!")
        
    else:
        print("You are very lucky! You've guessed the right \nnumber in first guess!")
        print("Time spent playing:", elapsed_time,"seconds.")
        print(separator)
        print("That's amazing!")