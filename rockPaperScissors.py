import random
print('welcome to the rock paper scissors play game:')
print('ready?')
print('GO')
user_input = 'y'

while user_input=='Y' or user_input=='y':

    print(' rock, paper, scissors')
    user_choice=input()
    computer_choice=random.choice(['rock', 'paper', 'scissors'])
    print(computer_choice)

    if user_choice=='rock' and computer_choice=='scissors':
            print('You won!')
    if computer_choice=='rock' and user_choice=='scissors':
            print('you lost!')
    if user_choice=='rock' and computer_choice=='paper':
            print('you lost!')
    if user_choice=='paper' and computer_choice=='rock':
            print('You won!')
    if user_choice=='paper' and computer_choice=='scissors':
            print('you lost!')
    if user_choice == 'scissors' and computer_choice == 'paper':
            print('you won!')
    print('do you want to continue? [y,n]')
    user_input=input()