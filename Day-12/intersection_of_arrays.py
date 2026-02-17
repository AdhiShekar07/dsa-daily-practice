"""
Problem: Intersection of Two Arrays II
Platform: LeetCode
Difficulty: Easy
Approach: Hashing (Frequency Map)
Time Complexity: O(n + m)
Space Complexity: O(n)
"""

def intersect(nums1, nums2):
    freq = {}
    result = []
    
    # Count frequency
    for num in nums1:
        freq[num] = freq.get(num, 0) + 1
    
    # Check in second array
    for num in nums2:
        if num in freq and freq[num] > 0:
            result.append(num)
            freq[num] -= 1
    
    return result
