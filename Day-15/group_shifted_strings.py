"""
Problem: Group Shifted Strings
Platform: LeetCode
Difficulty: Medium
Approach: Hashing (Pattern Key Formation)
Time Complexity: O(N * K)
Space Complexity: O(N)
"""

from collections import defaultdict


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        groups = defaultdict(list)

        for s in strings:

            # Create key based on shifting pattern
            key = []

            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                key.append(diff)

            groups[tuple(key)].append(s)

        return list(groups.values())