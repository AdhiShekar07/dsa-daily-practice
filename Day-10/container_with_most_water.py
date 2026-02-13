"""
Problem: Container With Most Water
Platform: LeetCode
Difficulty: Medium
Approach: Two Pointer
Time Complexity: O(n)
Space Complexity: O(1)
"""

height = list(map(int, input("Enter heights: ").split()))

left = 0
right = len(height) - 1
max_area = 0

while left < right:
    width = right - left
    h = min(height[left], height[right])
    area = width * h

    if area > max_area:
        max_area = area

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print("Maximum water:", max_area)
