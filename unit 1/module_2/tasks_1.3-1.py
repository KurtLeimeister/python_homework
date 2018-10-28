# Python academy, unit 1, module 2
# By Kurt, 2018-10-28

# Task 1: PRINT MORE THINGS
#[ ] increase the number of arguments used in print() to 8 or more
student_age = 17
student_name = "Hiroto Yamaguchi"
print(student_name,'will be in the class for',student_age, 'year old students.','5','6','7','8')

# Task 2: Capslock printing 1
# [ ] define (def) a simple function called yell_it() and call the function
phrase = 'Indentation matters'


# define yell_it. input: none; output: none
def yell_it():
    print(phrase.upper() + '!')
#call yell_it
yell_it()

# Task 3: defining a fundtion with input and default values
# [ ] define yell_this()
def yell_this(words_to_yell='default string'):
    print(words_to_yell.upper()+'!')
# [ ] get user input in variable words_to_yell
words_to_yell=input('Words to be shouted: ')
# [ ] call yell_this function with words_to_yell as argument
yell_this(words_to_yell)