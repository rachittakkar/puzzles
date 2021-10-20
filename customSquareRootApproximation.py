#author rachit, andreas
#3.10.21
import math
import re

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

#y = 1.0
def square_root(x):
    for y in range(10000000):
        if y*y == x:
            return y
        
        elif y == x:
            return ("no perfect square")

def square_root1(x):
    for y in range(10000000):
        if y*y > x:
            
            #4
            factor = y-1

            newfac=factor*factor
            
            #7
            #sqrts= square_root(factor)
            step2 = x - newfac

            #8
            step3=factor*2

            div = step2/step3
            
            #approximate result

            #mul=0.1*(div)      
            
            #4.875
            res = factor +  div 

            #-.75
            res1= x - (res*res) 

            #9.6
            res2=2*res

            div2 = res1/res2
            res3 = res +  div2 
            return res3
        
       # elif y == x:
          #  return ("no perfect square")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")
print("6.Sqaure root")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    elif choice in ('5','6'):
        num3 = float(input("Enter the number: "))
        #num4 = float(input("Enter second number: "))
        

        if choice == '5':
            print("square of ", num3, "=", multiply(num3,num3))

        elif choice == '6':
            print("square root of ", num3, "=", square_root1(num3))

        break

    else:
        print("Invalid Input")
        break