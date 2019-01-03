# Python academy, unit 1, module 4.2, first sheet
# By Kurt, 2019-01-03


# Task 1: Program: Get a name forever ...or until done
# create variable, familar_name, and assign it an empty string ("")
# use while True:
# ask for user input for familar_name (common name friends/family use)
# keep asking until given a non-blank/non-space alphabetical name is received (Hint: Boolean string test)
# break loop and print a greeting using familar_name
from typing import Any, Union

familiar_name = ""

while True:
    familiar_name = input('Please enter a non-blank name that does not contain spaces: ')
    if familiar_name.isalpha():
        print('A shoutout to '+ familiar_name)
        break

# [ ] Create the Shirt Count program, run tests
shirt_count = 0
s_count = 0
m_count = 0
l_count = 0
size_input = ""
max_shirts = 2
while True:
    shirt_count = s_count + m_count + l_count
    if shirt_count >= max_shirts:
        print('That\'s enough, noone needs more than', max_shirts, 'shirts!')
        break
    else:
        size_input = input('Please enter shirt size (S/M/L) or "e" to exit: ').lower()
        if size_input.startswith('e'):
            break
        elif size_input == 's':
            s_count += 1
        elif size_input == 'm':
            m_count += 1
        elif size_input == 'l':
            l_count += 1
        else:
            print('invalid entry, please enter valid shirt size or "e" to exit')

print('\n' + str(shirt_count), 'shirts: \nS: ', s_count, '\nM: ', m_count, '\nL: ', l_count)


# CHALLENGE: Shirt Register (optional)
# Update the Shirt Count program to calculate cost
#
# use shirt cost (S = 6, M = 7, L = 8)
# to calculate and report the subtotal cost for each size
# to calculate and report the total cost of all shirts

# [ ] Create the Shirt Register program, run tests

# number of shirts
shirt_count = 0
s_count = 0
m_count = 0
l_count = 0
# cost of one shirt in given size
s_price = 6
m_price = 7
l_price = 8

# maximum number of items in one order
max_shirts = 2
while True:
    shirt_count = s_count + m_count + l_count
    # check if maximum number of items per order has been reached / exceeded.
    if shirt_count >= max_shirts:
        print('That\'s enough, noone needs more than', max_shirts, 'shirts!')
        break
    # If maximum number was not exceeded, proceed
    else:
        # collect user input for shirt order
        size_input = input('Please enter shirt size (S/M/L) or "e" to exit: ').lower()
        # exit if input starts with e
        if size_input.startswith('e'):
            break
        elif size_input == 's':
            s_count += 1
        elif size_input == 'm':
            m_count += 1
        elif size_input == 'l':
            l_count += 1
        else:
            print('invalid entry, please enter valid shirt size or "e" to exit')

# cost of all shirts in given size
s_cost = s_price*s_count
m_cost = m_count*m_price
l_cost = l_count*l_price
total_cost = s_cost + m_cost + l_cost

print('\nsize\tnumber\tcost')
print('S\t' + str(s_count) + '\t' + str(s_cost))
print('M\t' + str(m_count) + '\t' + str(m_cost))
print('L\t' + str(l_count) + '\t' + str(l_cost))
print('Total\t' + str(shirt_count) + '\t' + str(total_cost))
