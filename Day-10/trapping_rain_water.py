"""
Problem: Trapping Rain Water
Platform: LeetCode
Difficulty: Hard
Approach: Brute Force (Left-Max & Right-Max)
Time Complexity: O(n²)
Space Complexity: O(1)
"""

height = list(map(int, input("Enter heights: ").split()))
n = len(height)

total_water = 0

for i in range(1, n - 1):

    # Find max on left
    left_max = height[i]
    for j in range(i):
        if height[j] > left_max:
            left_max = height[j]

    # Find max on right
    right_max = height[i]
    for j in range(i + 1, n):
        if height[j] > right_max:
            right_max = height[j]

    # Water at current index
    water = min(left_max, right_max) - height[i]

    if water > 0:
        total_water += water

print("Total trapped water:", total_water)
