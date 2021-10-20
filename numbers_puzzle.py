#numbers_puzzle

import time as t
import functools as f
import operator as o
import random as r
import math as m

print("Welcome to numbers game!!")
t.sleep(3)
print("Answer the following multiplication problems before time runs out!")
t.sleep(3)
print("Ready")
t.sleep(0.5)
print("3")
t.sleep(0.5)
print("2")
t.sleep(0.5)
print("1")
t.sleep(0.5)
print("go!!!")

starting_time = t.time()

score = 0

while True:
    difficulty = 2
    difficulty_progression = m.floor(score/10)
    overall_difficulty = difficulty + difficulty_progression

    list_of_numbers = []
    for i in range(overall_difficulty):
        number=r.randint(1,9)
        list_of_numbers.append(number)

    answer = f.reduce(o.mul , list_of_numbers,1)
    print("Multiply these numbers: ", list_of_numbers)   

    user_input = input()

    try:
    # try converting it to a number
        if answer == int(user_input):
            score = score + (1 * overall_difficulty)
            continue
        
        else:
            print('Game over! The answer was', answer)
            elapsed_time = t.time() - starting_time
            print('Your score was', score, 'in only', elapsed_time, " seconds.")
            break

    except ValueError:
    # ValueError is raised when that didn't work
        print("Please enter a number!")
    
    
   