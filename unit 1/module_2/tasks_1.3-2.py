# Python academy Unit 1 Module 3 part 2
# By Kurt, 2018-10-27


# Task 1: a function with an parameter
# create and call make_doctor() with full_name argument from user input - then print the return value
full_name=input('please enter your full name: ')
def make_doctor(name):
    return('Dr. '+name.title())
print(make_doctor(full_name))

# Task 2: A function with 3 parameters
# [ ] add a 3rd period parameter to make_schedule
# [ ] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)

def make_schedule(period1, period2, period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title())
    return schedule

print(make_schedule('1','2','3'))


# Task 2 bonus: a function with 6 parameters
# Since 1st, 2nd and 3rd are irregular, here's a list
order_of_lessons=['1st','2nd','3rd','4th','5th','6th']
# make_schedule_6 is meant to be called with up to 6 strings
def make_schedule_6(*args):
    # to be incremented, it is the (i+1)st period / parameter
    i=0
    # iterate over all parameters
    for p in args:
        # break if the current subject is the 7th or higher
        if i>5:
            print('up to 6 subjects supported')
            break
        # else, print the period and increment i
        else:
            print('['+order_of_lessons[i]+'] '+p.title())
            i+=1

make_schedule_6('1','2','3','4','5','6','7')