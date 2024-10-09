import random
'''
1 for snake
-1 for water
0 for gun
'''
computer =  random.choice([-1, 0, 1])
youStr= input("Enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
revDict={1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youStr]

print(f"You choose {revDict[you]} \ncoumputer choose {revDict[computer]} ")

if(computer == you):
    print("Draw")
elif(computer == -1 and you == 1):
    print("You Win!")
elif(computer == -1 and you == 0):
    print("You Lose!")
elif(computer == 1 and you == -1):
    print("You Lose!")
elif(computer == 1 and you == 0):
    print("You Win!")
elif(computer == 0 and you == -1):
    print("You Win!")
elif(computer == 0 and you == 1):
    print("You Lose")
else:
    (print("Something went wrong"))