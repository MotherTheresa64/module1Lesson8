""" Project 1: Create a function "introduce_yourself" that takes a name and favorite
hobby. the function should print a greeting and mention the person's hobby. """
#Define the function
def introduce_yourself(name, hobby):
    print(f"Hey {name}, your hobby of {hobby} is cool!")
#Ask the user for their name and hobby 
name = input(str("What's your name? "))
hobby = input(str("what's your hobby? "))
#Call the function with the given input user's name and hobby
introduce_yourself(name, hobby)

"""Final Challenge: Create a function that takes a list of numbers 
as an argument, squares each number, and returns a new list with the squared values."""


list_of_numbers = [3, 99, 12, 1, 7]

def square_numbers(numbers):
#Create an empty list to store the squared numbers
    squared_numbers = []
#Iterate over the list of numbers and square each number
    for number in numbers:
#Append the squared number to the list
        squared_numbers.append(number ** 2)
#Return the list of squared numbers
    return squared_numbers
#Call the function with the list of numbers and print the result
squared_list = square_numbers(list_of_numbers)
print(squared_list)
