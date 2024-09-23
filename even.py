def is_even(number):
    return number % 2 == 0

# Get user input
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of numbers (as strings)
numbers = input_numbers.split()

# Convert the list of strings to a list of integers
numbers = [int(num) for num in numbers]

# Filter and print even numbers
even_numbers = [num for num in numbers if is_even(num)]

print("Even numbers:", even_numbers)
