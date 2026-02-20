"""
Problem: Two Sum
Platform: LeetCode
Difficulty: Easy
Approach: Hash Map
Time Complexity: O(N)
Space Complexity: O(N)
"""


class Solution(object):
    def twoSum(self, nums, target):

        hashmap = {}  # value -> index

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i