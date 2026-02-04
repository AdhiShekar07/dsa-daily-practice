"""
Problem: Count Frequency of Elements in an Array
Platform: GeeksforGeeks
Difficulty: Easy
Approach: Hashing (Dictionary)
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def countFreq(self, arr):
        freq = {}

        for element in arr:
            if element in freq:
                freq[element] += 1
            else:
                freq[element] = 1

        return freq
