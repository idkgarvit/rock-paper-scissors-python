import random 
computer = random.choice([1 , -1 , 0])
your_choice = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()
dict = {"r" : 1 , "p" : -1 , "s" : 0  }
reverseDict = { 1 : "Rock" , -1 : "Paper" , 0 : "Scissor" }

if your_choice not in dict :
    print("Invalid input! Please enter r, p, or s.")
    exit()

you = dict[your_choice]

print("You choose :" , reverseDict[you] )
print("Computer choose :" , reverseDict[computer])

if (computer == you ):
    print("It's a draw . ")
else:
    if (computer == 1 and you == -1 ):
        print("You win! ")
    elif(computer == 1 and you == 0 ):
        print("You loose!")
    elif (computer == -1 and you == 1 ):
        print("You loose! ")
    elif(computer == -1 and you == 0 ):
        print("You win! ")
    elif (computer == 0 and you == 1 ):
        print("You win! ")
    elif(computer == 0 and you == -1 ):
        print("You loose! ")
    else :
        print("Something went wrong .")
