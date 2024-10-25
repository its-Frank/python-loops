##Given a tuple of numbers, e.g., (10, 20, 30, 40, 50), write a Python function using a loop that returns the largest number in the tuple.
def find_largest_number(num_tuple):
    largest = num_tuple[0]  # Assume the first number is the largest initially
    for num in num_tuple:
        if num > largest:
            largest = num
    return largest
# Example usage
example_tuple = (10, 20, 30, 40, 50)
largest_number = find_largest_number(example_tuple)
print(largest_number)  # Output: 50
