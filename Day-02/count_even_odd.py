"""
Problem: Count Even and Odd Numbers in an Array
Platform: GeeksforGeeks
Difficulty: Easy
Approach: Traversal with Condition Check
Time Complexity: O(n)
Space Complexity: O(1)
"""

def count_even_odd(arr):
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count
