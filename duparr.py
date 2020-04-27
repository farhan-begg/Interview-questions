'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 1
        while r < len(nums):
            while r < len(nums) and nums[l] == nums[r]:
                r += 1
            if r < len(nums):
                nums[l+1] = nums[r]
                l += 1
                r += 1
        return l+1


'''
        Variable Table 
        nums = [array]
        l 0
        r 1
        num l + 1 = nums[r]
        l +=1
        r =+ 1
'''
