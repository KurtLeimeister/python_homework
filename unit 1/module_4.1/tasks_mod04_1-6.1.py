# Python academy, unit 1, module 3.2, first sheet
# By Kurt, 2018-11-21

# Task 1: Say "Hello" with nested if
# [ ] Challenge: handle input other than y/n

sayHi=input('Say "Hello"? y/n: ').lower()
if sayHi=='y':
    fullHello=input('Full "Hello"? y/n: ').lower()
    if fullHello=='y':
        print('Hello')
    elif fullHello=='n':
        print('hi')
    else:
        print("I'm not sure what to say...")
elif sayHi=='n':
    print('(Friendly Nod)')
else:
    pass

# Task 2:  Create the "Guess the bird" program
# first variant: unknown which birds are in bird_names
bird_names="Eagle, Sparrow, Pidgeon, Ostrich, Falcon, Owl, Woodpecker"
guesses=5
for guess in range(1,guesses+1):
    bird_guess=input('Guess the bird: ')
    # This gives some very unexpected results...
    guess_correct=(bird_guess in bird_names)
    if guess_correct:
        print('Correct in '+str(guess)+' try!')
        break
    elif guess==guesses:
        print('Sorry, out of tries.')