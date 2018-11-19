# Python academy, unit 1, module 3.2, second sheet
# By Kurt, 2018-11-19

# Task 1: basic math
# [ ] print the result of subtracting 15 from 43
print(15-43)
# [ ] print the result of multiplying 15 and 43
print(14*43)
# [ ] print the result of dividing 156 by 12
print(156/12)
# [ ] print the result of dividing 21 by 0.5
print(21/0.5)
# [ ] print the result of adding 111 plus 84 and then subtracting 45
print(111+84-45)
# [ ] print the result of adding 21 and 4 and then multiplying that sum by 4
print((21+4)*4)


# Task 2: Integer String Multiplication
# [ ] create and test multiply() function
def multiply(factor1,factor2):
    factor1=int(factor1)
    factor2=int(factor2)
    # less boring than str(factor1*factor2)
    return(str(factor1)*factor2)

print(multiply('9','3'))

# Task 3: Improved Multiplication

# [ ] create improved multiply() function and test with /, no argument, and an invalid operator ($)
# [ ] create and test multiply() function
# I had to look up default values, should probably hurry up with those exercises
def multiply2(factor1,factor2,operator='*'):
    factor1=int(factor1)
    factor2=int(factor2)
    # Check what the operator is
    # Couldn't find a way to take a non-string operator like *
    if operator=='*':
        return(str(factor1*factor2))
    elif operator=='/':
        return(str(factor1/factor2))
    else:
        return('Invalid Operator')
# backslash not esccaped -_-
print(multiply2('2','3','/'))


# Task 4: Review, run, fix
student_name = input("enter name: ").capitalize()
if student_name.startswith("F"):
    print(student_name,"Congratulations, names starting with 'F' get to go first today!")
    # added colon after elif condition
elif student_name.startswith("G"):
    print(student_name,"Congratulations, names starting with 'G' get to go second today!")
else:
    print(student_name, "please wait for students with names staring with 'F' and 'G' to go first today.")
