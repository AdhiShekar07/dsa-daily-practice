"""
Problem: 3Sum Closest
Platform: LeetCode
Difficulty: Medium
Approach: Sorting + Two Pointer
Time Complexity: O(n²)
Space Complexity: O(1)
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest if better
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum   # Exact match
        
        return closest_sum
