#standard_change_maker

def number_of_coins(a):
    coins = [50,25,10,5,1]
    count = 0

    for x in coins:
        while a >= x:
            a=a-x
            count += 1

    return count

while True:    
    money = int(input("\n\nHow much money you got? "))
    print("you get " + str(number_of_coins(money)))

