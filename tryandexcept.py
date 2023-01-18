# To handle certain possible errors I can use Try and Except.
# I can include the block of code I want to run under "try:"
# If an error is passed under the "try:" block, it will then return a message for the error.

# start with try:
# Created a list with 3 values.
# Attempted to replace a value in the list using a certain index.
# Since that index does not exist, it then runs the code under "except:"
try:
    lista = ['Fruit', 'Vegetable', 'Meat']
    lista[3] = 'Dessert'
except IndexError:
    print("Sorry! We can't replace that value because it doesn't exist. Try entering the value 0, 1, or 2 instead.")
