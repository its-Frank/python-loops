#Write a function that takes a list of tuples as input, where each tuple contains two elements: a string and an integer
def tuples_to_dict(tuples_list):
    result_dict = {}
    for string, number in tuples_list:
        result_dict[string] = number
    return result_dict
# Example usage
example_tuples = [("apple", 5), ("banana", 3), ("cherry", 7)]
result = tuples_to_dict(example_tuples)
print(result)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}
