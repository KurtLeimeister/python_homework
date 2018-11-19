# Python academy, unit 1, module 3.2, first sheet
# By Kurt, 2018-11-19

# Task 1: elif
# Fun fact: Elif was the first name of one of my class mates in highschool

# [ ] code and test SHIRT SALE
size=input('Please enter shirt size (S/M/L): ').upper()
if size == 'S':
    print('Small = $6')
elif size == 'M':
    print('Medium = $7')
elif size == 'L':
    print('Large = $8')
else:
    print('Not available. Available sizes: S, M, L.')


# Task 2: casting with int and str


# 2.a: 2 ints 1 str
str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as integers and print the result
print(int(str_num_1)+int(str_num_2)+int_num_3)

# 2.b 2 strs 1 int
str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as test strings and print the result
print(str_num_1+str_num_2+str(int_num_3))

# 2.c: this one was already in the notebook...
# [ ] code and test: adding using int casting
str_integer = "2"
int_number = 10
number_total = int(str_integer) + int_number
print(number_total)



# Task 3: adding calculator (more of the same)
# [ ] code and test the adding calculator
numba_one=int(input('Please enter an integer between 9 and 9: '))
numba_two=int(input('Please enter the age of Garfield (int): '))

print(str(numba_one),'+',str(numba_two),'=',str(numba_one+numba_two))