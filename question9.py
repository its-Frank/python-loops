#Write a Python function that accepts a list of integers and a target sum.
def has_pair_with_sum(nums, target_sum):
    seen_numbers = {}
    for num in nums:
        complement = target_sum - num
        if complement in seen_numbers:
            return True
        seen_numbers[num] = True
    return False
# Example usage
example_list = [10, 15, 3, 7]
target = 17
result = has_pair_with_sum(example_list, target)
print(result)  # Output: True
