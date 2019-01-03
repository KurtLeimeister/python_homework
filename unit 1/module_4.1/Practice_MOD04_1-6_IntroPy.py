# Python academy, unit 1, module 4.1, practice sheet
# By Kurt, 2018-12-05


# Task 1: printing stuff with escaped characters

# [ ] print a string that outputs the following exactly: The new line character is "\n"
print('The new line character is "\\n"')

# [ ] print output that is exactly (with quotes): "That's how we escape!"
print('"That\'s how we escape!"')

# [ ] with only 1 print statement and using No Space Characters, output the text commented below
# 1       one
# 22      two
# 333     three
print('1\tone\n22\ttwo\n333\tthree')

# Task 2: quote_me function
# quote_me takes a string argument and returns a string that will display surrounded with added double quotes if
# printed
#
# check if passed string starts with a double quote ("\""), then surround string with single quotations
# if the passed string starts with single quote, or if doesn't start with a quotation mark
# then surround with double quotations


# [ ] create and test quote_me()
def quote_me(string):
    if string.startswith('"'):
        return string
    else:
        return '\"' + string + '\"'


# Test the function code passing string input as the argument to quote_me()
print(quote_me("Simple string"))
print(quote_me("\"String  starting with an explicit escaped double quote"))
print(quote_me('"Single quoted string starting with a double quote'))


# Task 3: shirt order

# First get input for color and size
#
# White has sizes L, M
# Blue has sizes M, S
# print available or unavailable, then
# print the order confirmation of color and size
#
# change to True if color and size are avaliable*

def shirt_order():
    color = input('Please enter color (White / Blue): ').upper()
    size = input('please enter size (S/M/L)').upper()
    # check if shirt is available
    available = False
    if color == 'WHITE':
        if size in ['L', 'M']:
            available = True
    elif color == 'BLUE':
        if size in ['M', 'S']:
            available = True
    # print whether order was taken
    if available:
        print('Your order was confirmed.')
    else:
        print('Sorry, the size and color you ordered are not available at the moment')
    # shout the customers order
    print('\nSize:\t'+size+'\nColor:\t'+color)


shirt_order()


# Task 4:  str_analysis() Function
# Create the str_analysis() function that takes a string argument. In the body of the function:
#
# Check if string is digits
# if digits: convert to int and check if greater than 99
# if greater than 99, print a message about a "big number"
# if not greater than 99, print message about "small number"
# if not digits: check if string isalpha
# if isalpha print message about being all alpha
# if not isalpha print a message about being neither all alpha nor all digit
# call the function with a string from user input

def str_analysis(string):
    if string.isdigit():
        number = int(string)
        if number > 99:
            print('much number such wow')
        else:
            print('What\'s that, a number for ants?')
    elif string.isalpha():
        print('that\'s a word, not a number')
    else:
        print(string+' is neither an integer nor a word...')


str_analysis(input('\nPlease enter an integer: '))


# Task 5:Program: ticket_check() - finds out if a seat is available¶
# Call ticket_check() function with 2 arguments: section and seats requested and return True or False
#
# section is a string and expects: general, floor
# seats is an integer and expects: 1 - 10
# Check for valid section and seats
#
# if section is general (or use startswith "g")
# if seats is 1-10 return True
# if section is floor (or use starts with "f")
# if seats is 1-4 return True
# otherwise return False

def ticket_check(section, seats):
    section__lower = str(section).lower()
    valid_section = section__lower in ['general', 'floor']
    valid_seats = False
    if seats.isdigit():
        if 1 <= int(seats) <= 10:
            valid_seats = True
    if valid_section and valid_seats:
        if section__lower.startswith("g"):
            return True
        if section__lower.startswith('f'):
            if int(seats) <= 4:
                return True
    else:
        return False


desired_section = input('\nPlease enter section (general / floor): ')
desired_seats = input('How many seats? (1-10): ')

print(ticket_check(desired_section, desired_seats))
