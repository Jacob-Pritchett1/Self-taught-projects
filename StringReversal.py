# Reversing a string


# We can start by creating an empty string.
reversed_stringy = " "
# We can then ask for input from a user and save it to the variable "stringy"
stringy = input("Enter a word or phrase here: ")
# We can then make reversed_stringy equal to stringy, but backwards.
# [::1] is known as slicing. [start:stop:step]. So we want to take the entire
# string (ex:[:]), but we want our step to be [-1] which returns the listt, but
# is a negative index. So we start with the last letter, and then work our way to
# the first letter.
reversed_stringy = stringy[::-1]
# Next, we just print reversed_stringy to the terminal.
print(reversed_stringy)


# Also, we could build a function to take care of it, if I needed to do it more than once.

# create my function with stringy as my parameter.
# then return it instead of printing it so I can save it to a variable.
# then I can invoke the function and save my text to it.
# print it to the terminal.

# def reversal(stringy):
# return stringy[::-1]


#new_reversal = reversal("Our shadows taller than our souls")

# print(new_reversal)
