# FizzBuzz Project

# The problem: Print every number from 1 to 100 (both included) on a new line.
# Numbers which are multiple of 3, print “Fizz” instead of a number.
# For the numbers which are multiples of 5, print “Buzz” instead of a number.
# For the number which is multiple of both 3 and 5, print “FizzBuzz” instead of numbers.

# First step: Create a for loop that can iterate over a list of 1 to 100.
# Use the range function to create a start and end of a defined range of numbers.
# I use 101 instead of 100 as the second (start,stop,step) would print UP TO 101, not including it.
for num in range(1, 101):
    # Use an if statement with "and" to meet the requirement of both 3 and 5.
    # I choose to use 3 and 5 rather than 15 to practice.
    # I could use if num % 15 == 0: to make the code more efficient.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # use elif (else-if) to run through the next iteration I want to find.
    elif num % 3 == 0:
        print("Fizz")
    # use elif (else-if) to run through the last iteration I need to find.
    elif num % 5 == 0:
        print("Buzz")
    # use an else here to return all numbers that don't meet me requirements in me if/elif statements.
    else:
        print(num)
