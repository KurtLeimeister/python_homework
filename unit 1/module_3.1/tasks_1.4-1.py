# Python academy, unit 1, module 3, first sheet
# By Kurt, 2018-11-07

# Task 1: if, else
sunny_today = True
# [ ] test if it is sunny_today and give proper responses using if and else
# weather_test(bool sunny): null
def weather_test(sunny):
    if sunny:
        print('What a mighty fine day, let\'s go outside!')
    else:
        print('Let\'s stay inside today')

print('calling function weather_test with input True')
weather_test(sunny_today)
print()

sunny_today=False
print('calling function weather_test with input False')
weather_test(sunny_today)

# Task 2: more if, else
test_string_1 = "welcome"
test_string_2 = "I have $3"
# [ ] use if, else to test for islower() for the 2 strings
def is_it_low(string):
    if string.islower():
        print('yes it is')
    else:
        print('no, it ain\'t')
print('is test_string_1 lowercase?')
is_it_low(test_string_1)
print('is test_string_2 lowercase?')
is_it_low(test_string_2)

print()

# Task 2 part b: if, else inside a function
test_string_1 = "welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"
# [ ] create a function w_start_test() use if & else to test with startswith('w')
def w_start_test(string):
    if string.lower().startswith('w'):
        print('"'+string+'" starts with the letter w.')
    else:
        print('Nope.')
# [ ] Test the 3 string variables provided by calling w_start_test()
w_start_test(test_string_1)
w_start_test(test_string_2)
w_start_test(test_string_3)


