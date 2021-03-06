# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# restate question
# if i was given an array of integers you like me to return two numbers that add up to the target value?

# clarifying questions
# are the numbers sorted?
# can the target value be negative

# assumption
# the list is not sorted
# target can equal - numbers

# number 2 should equal target number - number 1
# loop through the pairs of number in each list
# return index number 1 and number 2
# Does time complexity matter does memory storage matter?


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


# Given a 32-bit signed integer, reverse digits of an integer.

# Restate
# If I was given an integeer you want me to figure out how to reverse the digits?


# clarifying questions
# are the numbers sorted
# am i given the numbers in a list?
# can the numbers return zero
# are the numbers negative?

# assumtions
# the numbers are not sorted
# the numbers can't return zero
# numbers can be zero
# and numbers doesn't matter


# for example if the number was 321
# what I would do is append the last number into a new list until its over (naive answer)
# or use the int to string method and than reverse the integer
# Does time complexity matter, Does memory matter?
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x >= 0:
        x = int(str(x)[::-1])
    else:
        x = -int(str(-x)[::-1])
    return x if x <= (2**31-1) and x >= -(2**31) else 0


print(reverse(x=132))
