# Python academy unit 1 module 1.2-4
# Kurt, 2018-10-20

# Task 1 - format with .capitalize(), .lower(), .upper(), .swapcase()
# [ ] get input for a variable, fav_food, that describes a favorite food
fav_food = 'Blaukraut'
# [ ] display fav_food as ALL CAPS, used in a sentence
print('My favorite food? '+fav_food.upper()+'!')
# [ ] dispaly fav_food as all lower case, used in a sentence
print('In German,', fav_food.lower(), 'is always capitalized, just like all nouns.')
# [] display fav_food with swapped case, used in a sentence
print('tODAY IS OPPOSITE DAY, SO WE EAT', fav_food.swapcase())
# [] display fav_food with capitalization, used in a sentence
print(fav_food.capitalize(),'bleibt',fav_food.capitalize(),'und Brautkleid bleibt Brautkleid')

print()
fav_color = "Forest Green"
# [] display the fav_color variable as upper, lower, swapcase, and capitalize formatting
# in a single print() statement
print('returning fav_color with the following formatting:')
print('upper, lower, swapcase, and capitalize')
print(fav_color.upper(), fav_color.lower(), fav_color.swapcase(), fav_color.capitalize())


print()
# Task 2: format   input() with .upper()
# [] input variable fav_color as upper
fav_color=input('What is your favorite color?: ').upper()
# [] print fav_color
print(fav_color)


print()
#Task 3: using 'A in B' to test if string A is contained in string B
print()
# Task 3.1 - with description text, testing the menu variable for:
# 'pizza', 'soup' and 'dessert'
menu = "salad, pasta, sandwich, pizza, drinks, dessert"

for food in ['pizza', 'soup', 'dessert']:
    print("Menu contains "+food+':',food in menu)

print()
#Task 3.2: Create a program where the user supplies input to search the menu
def is_on_menu(current_menu):
    print('This program can check if a specific food is in the menu.')
    # collect input: food item to check
    food_item = input('Food item to check: ')
    print()
    # check if current_menu contains food_item, ignoring capitalization
    if(food_item.upper() in current_menu.upper()):
        # if it is contained, print affirmative message
        print('The menu contains '+food_item.lower()+'.')
    else:
        # if it is not contained, print negative message
        print('Sorry, the menu does not contain '+food_item.lower()+'.')
# check if string enetered by user is in menu
is_on_menu(menu)

print()
# Task 3.3 (challenge) add to the Menu
# define string variable 'menu' in case it is not defined or not a string
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
# defining function add_to_menu which asks for input to add to 'menu'
# takes no parameters and returns a string
# it is assumed that the variable 'menu' exists and is a string
def add_to_menu():
    # print the current menu
    print('The current menu contains:')
    print(menu)
    # check if user wants to add something to the menu
    #skipping for now

    #prompt user for what they want to ask
    food_to_add = input('Which food should be added to the menu? ')
    #append food_to_add to menu, return the result
    # using lowercase since original menu is in lowercase
    return menu + ', ' + food_to_add.lower()
# define new_menu by adding to menu
new_menu = add_to_menu()
print()
print('the new menu contains:')
print(new_menu)

print()
# Task 3.4 - testing add_to_menu
# create user input to search for an item on the new menu
# Explaining what will be checked
print('Checking the new menu')
# well, here reusing actually makes sense
is_on_menu(new_menu)

# Task 4 - fix the error
paint_colors = "red, blue, green, black, orange, pink"
# added quotation marks to 'red'
print('Red in paint colors = ','red' in paint_colors)
