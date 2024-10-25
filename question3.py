##Given the list nums = [1, 2, 3, 4, 5], write a Python function using a loop that returns the sum of all the numbers in the list.
def sum_of_list(nums):
    total = 0
    for num in nums:
        total += num
    return total
# Example usage
nums = [1, 2, 3, 4, 5]
print(sum_of_list(nums))  # Output: 15
