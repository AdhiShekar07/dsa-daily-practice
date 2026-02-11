"""
Problem: Maximum Subarray Sum
Platform: LeetCode / GFG
Difficulty: Medium
Approach: Kadane's Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = list(map(int, input("Enter elements: ").split()))

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print("Maximum Subarray Sum:", max_sum)
