"""
Problem: Check if One String is a Subsequence of Another
Platform: LeetCode / GFG
Difficulty: Easy
Approach: Two Pointer
Time Complexity: O(n)
Space Complexity: O(1)
"""

s = input("Enter first string: ")
t = input("Enter second string: ")

i = 0  # pointer for s

for ch in t:
    if i < len(s) and s[i] == ch:
        i += 1

if i == len(s):
    print(True)
else:
    print(False)
