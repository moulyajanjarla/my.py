import random
list_1 = ['R','P','S']
list_2 = ['R','P','S']
num = random.choice(list_1)
num1=random.choice(list_2)
num3=[num,num1]
def calculate():
    for i in num3:
        if num3[0]=='R' and num3[1]=='P'or num3[0]=='P' and num3[1]=='S' or num3[0]=='S' and num3[1]=='R':
            print("player 2 wins")
        elif num3[0]=='S' and num3[1]=='P' or num3[0]=='R' and num3[1]=='S' or num3[0]=='P' and num3[1]=='R':
            print('player 1 wins')
        elif num3[0]==num3[1]:
            print('you got draw')
            return calculate
print('^..^|Come On lets have some fun|^..^')
print('enter either 1or2  choose your play')
for i in range(2):
    i=int(input())
    if i==1:
        print('you picked one random number',num)
        print('enter another number')
    elif i==1:
        print('you have picked a randm one',num1)
        print('enter another number')
    elif i==2:
        print('you have picked a randm one',num)
        print('enter another number')
    elif i==2:
        print('you have picked a randm one',num1)
        print('enter another number')
    else:
        print('choose valid number')
print('you both got these values',num3)
calculate()


