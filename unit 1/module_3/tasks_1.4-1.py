# Python academy, unit 1, module 3.1
# By Kurt, 2018-11-14

# Task 1: if, else
# Give a weather report using `if, else`


# [ ] test if it is sunny_today and give proper responses using if and else
def what_to_do(weather):
    if weather:
        print("Let's go outside and enjoy the sun!")
    else:
        print("Today would be a good day to bake a cake.")

sunny_today = True
# zefrank1 - true facts about the ... - https://www.youtube.com/watch?v=st8-EY71K84
print('This is how the octopus do')
what_to_do(sunny_today)

sunny_today = False
# now with not-sunny weather
print("Spartans! What do we do when it's rainy?")
what_to_do(sunny_today)
print()

# Task 2: Evaluating Boolean Conditionals
test_string_1 = "welcome"
test_string_2 = "I have $3"
# [ ] use if, else to test for islower() for the 2 strings
def cheer_if_not_lower(string):
    if string.islower():
        print("How boring, '"+string+"' is all lowercase")
    else:
        print("CaPiTaL lETteRs ArE so coOl")

print("testing test_string_1 and test_string_2 for lowercase")
cheer_if_not_lower(test_string_1)
cheer_if_not_lower(test_string_2)


# Task 2 continued
test_string_1 = "welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"
# [ ] create a function w_start_test() use if & else to test with startswith('w')
def w_start_test(string):
    if string.lower().startswith('w'):
        print('"'+string+'" starts with the letter "w".')
    else:
        pass
# [ ] Test the 3 string variables provided by calling w_start_test()
w_start_test(test_string_1)
w_start_test(test_string_2)
w_start_test(test_string_3)