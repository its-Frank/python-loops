#Write a function that accepts a list of strings and returns a new list where each string is reversed.
def reverse_strings(string_list):
    reversed_list = []
    for string in string_list:
        reversed_list.append(string[::-1])
    return reversed_list
#example
input_list = ["apple", "banana", "cherry"]
output_list = reverse_strings(input_list)
print(output_list)  # Output: ['elppa', 'ananab', 'yrrehc']
