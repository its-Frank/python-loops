#Write a function that takes a dictionary and an integer n as input and returns a list of keys from the dictionary where the value is greater than n.
def keys_greater_than_n(input_dict, n):
    keys_list = []
    for key, value in input_dict.items():
        if value > n:
            keys_list.append(key)
    return keys_list
# Example usage
example_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
result = keys_greater_than_n(example_dict, n)
print(result)  # Output: ['a', 'b']
