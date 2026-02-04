"""
Problem: Count Frequency and Return as List of Pairs
Platform: GeeksforGeeks
Difficulty: Easy
Approach: Hashing + Traversal
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

        result = []
        for key in freq:
            result.append((key, freq[key]))

        return result
