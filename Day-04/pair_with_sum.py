"""
Problem: Pair with Given Sum
Platform: GeeksforGeeks
Difficulty: Easy
Approach: Brute Force (Nested Loops)
Time Complexity: O(n²)
Space Complexity: O(1)
"""

def pair_with_sum(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True

    return False
