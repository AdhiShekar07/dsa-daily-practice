"""
Problem: Check if an Array is Sorted
Platform: GeeksforGeeks
Difficulty: Easy
Approach: Single Pass Comparison
Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = list(map(int, input("Enter elements: ").split()))

is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")
