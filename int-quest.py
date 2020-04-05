# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def twosum_indices_linear(nums, target):
    numtoindexmap = {}
    for num1_index, num1 in enumerate(nums):
        num2 = target - num1
        try:
            num2_index = numtoindexmap[num2]
        except KeyError:
            numtoindexmap[num1] = num1_index
        else:
            return num1_index, num2_index


print(sorted(twosum_indices_linear([2, 7, 11, 15], 18)))
