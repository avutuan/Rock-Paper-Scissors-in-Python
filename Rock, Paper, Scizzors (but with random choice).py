import random
x=0
while x<1:
    print("We're going to play Rock, Paper, Scizzors!")
    print('''1) Rock
2) Paper
3) Scizzors''')
    choice=input('Choose an option: ')
    print('')
    choice=choice.strip()
    choice=choice.removesuffix('!')
    choice=choice.removesuffix('?')
    choice=choice.removesuffix('.')
    choice=choice.lower()
    game=['rock', 'paper', 'scizzor']
    computer_choice=random.choice(game)
    if choice=='1':
        choice='rock'
    if choice=='2':
        choice='paper'
    if choice=='3':
        choice='scizzor'
        
    if choice==computer_choice:
        print('You chose', choice)
        print('I also chose', computer_choice)
        print('We tied')
        
    if choice=='rock' and computer_choice=='paper':
        print('You chose', choice)
        print('I chose', computer_choice)
        print('I win')
    if choice=='paper' and computer_choice=='scizzor':
        print('You chose', choice)
        print('I chose', computer_choice)
        print('I win')
    if choice=='scizzor' and computer_choice=='rock':
        print('You chose', choice)
        print('I chose', computer_choice)
        print('I win')
        
    if choice=='rock' and computer_choice=='scizzor':
        print('You chose', choice)
        print('I chose', computer_choice)
        print('I lost')
    if choice=='paper' and computer_choice=='rock':
        print('You chose', choice)
        print('I chose', computer_choice)
        print('I lost')
    if choice=='scizzor' and computer_choice=='paper':
        print('You chose', choice)
        print('I chose', computer_choice)
        print('I lost')
    print('')
    choice2=input('Wanna play again?: ')
    choice2=choice2.strip()
    choice2=choice2.removesuffix('!')
    choice2=choice2.removesuffix('?')
    choice2=choice2.removesuffix('.')
    choice2=choice2.lower()
    yes=['yes','yup','yah','yessir',"yes ma'am",'yuppers','yemen','yes sir','y','ye']
    no=['no','nope','nah','nopers','no sir',"no ma'am",'nuh','nephilim','n']
    if choice2 in yes:
        x=0
        print('')
    elif choice2 in no:
        x=1
    else:
        print("You didn't really answer so I'll take that as a no")
        x=1
