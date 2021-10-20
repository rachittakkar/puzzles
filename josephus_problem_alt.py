#Josephus problem using a mathematical tick suggested in the video lecture 
#https://www.youtube.com/watch?v=uCsD3ZGzMgE

while(True):

    choice = int(input("\n\nHow many people are stiitng in the circle? "))

    num = f'{choice:08b}' #convert the input number to binary

    list_of_people = list(num)

    for i in range(0,len(list_of_people)):

        list_of_people.remove('1') #remove the first high bit

        list_of_people.append('1') #append it at the end

        break

    survivor = ''.join(list_of_people) #join the new binary string

    print("\n\nThe person sitting at seat #",int(survivor, 2),"will be the survivor.") #convert the binary string to a number
   
