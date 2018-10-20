#Python academy unit 1 module 1.2-2
# Kurt, 2018-10-19

# Task 1: print 3 strings using comma separation
print("sting 1","string 2","String 3")

# Task 2: combining numbers and strings in print()
# Kieran had large feet at age 9...
print("Showsize:", 9, "| age:", 9)

# Task 3: collecting and displaying information
# [ ] get user input for a street name in the variable, street
street=input("Please enter street name: ")
# [ ] get user input for a street number in the variable, st_number
st_number=input("Please enter house number: ")
# [ ] display a message about the street and st_number
print("Adress:",street,st_number)
# Python 2: input() does not always return string
# i.e. can pass variables, strings need ""


# Task 4: more printing

# [ ] define a variable with a string or numeric value
# why not 2 strings...
variable = ['v', 'a', 'r']
# [ ] display a message combining the variable, 1 or more literal strings and a number
print(variable, 'iable and a number: ', 7)


# Task 5: the 'training organzer program'

# [ ] get input for variables: owner, num_people, training_time  - use descriptive prompt text
owner = input("enter name of training group organizer: ")
num_people = input("enter the number of attendees: ")
training_time = input("enter the starting time of the training: ")
# [ ] create a integer variable min_early and "hard code" the integer value (e.g. - 5, 10 or 15)
min_early = 15
# [ ] print reminder text using all variables & add additional strings -  use comma separated print formatting
print()
print('########################')
print()
print('Reminder: training for',num_people,'attendees is scheduled at'\
,training_time,', contact',owner,'')
print()
print('please arrive',min_early,'minutes before the scheduled time.')
