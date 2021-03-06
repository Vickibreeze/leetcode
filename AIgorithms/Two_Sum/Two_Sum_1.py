'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}

        for i in range(0, len(nums)):
            nums_dict[nums[i]] = i

        for i in range(0, len(nums)):
            another_num = target - nums[i]
            if another_num in nums_dict.keys() and \
                nums_dict.get(another_num) != i:
                return [i, nums_dict.get(another_num)]
        
        print("No such two numbers")
