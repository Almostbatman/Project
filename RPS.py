import random
print('Welcome To Rock Paper Scissors against Computer')
while True:
    a=int(input('Enter your choice [0,1,2] :'))
    if (a==0):
     print('You have Selected Rock')
     break
    elif(a==1):
     print('You have Selected Paper')
     break
    elif(a==2):
     print('You have Selected Scissors ')
     break
    else:
     print('You have entered an incorrect option')
     continue
comp=random.randint(0,2)
if(comp==0):
    print('Computer selected Rock')
elif(comp==1):
    print('Computer selected Paper')
else:
    print('Computer selected Scissor')
if(a==comp):
    print('Null')
elif(a==0 and comp==1):
    print('Computer Wins :(')
elif(a==0 and comp==2):
    print('You win!')
elif(a==1 and comp==0):
    print('You win!')
elif(a==1 and comp==2):
    print('Computer Wins :(')
elif(a==2 and comp==0):
    print('Computer Wins :(')
elif(a==2 and comp==1):
    print('You win!')