# Python academy, unit 1, module 3.2, first sheet
# By Kurt, 2018-11-22


# Task 1: create and test pre_word()
def pre_word(word):
    lword = word.lower()
    if lword.isalpha() and lword.startswith('pre'):
        return True
    else:
        return False


# Task 2
#
# Program: pre_word() Function
# Function has a single string parameter that it checks s is a single word starting with "pre"
#
# Check if word starts with "pre"
# Check if word .isalpha()
# if all checks pass: return True
# if any checks fail: return False
# Test
# get input using the directions: *enter a word that starts with "pre": *
# call pre_word() with the input string
# test if return value is False and print message explaining not a "pre" word
# else print message explaining is a valid "pre" word|
if not pre_word(input('enter a word that starts with "pre":')):
    print('not a "pre" word')
else:
    print('It starts with "pre"')