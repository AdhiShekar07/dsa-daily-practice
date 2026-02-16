"""
Problem: Find Saddle Point in a Matrix
Platform: GeeksforGeeks
Difficulty: Medium
Approach: Row Min + Column Max Check
Time Complexity: O(n²)
Space Complexity: O(1)
"""

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rows = len(matrix)
cols = len(matrix[0])

found = False

for i in range(rows):

    # Step 1: Find minimum in row
    min_val = min(matrix[i])
    col_index = matrix[i].index(min_val)

    # Step 2: Check if it is maximum in that column
    is_saddle = True

    for k in range(rows):
        if matrix[k][col_index] > min_val:
            is_saddle = False
            break

    if is_saddle:
        print("Saddle Point:", min_val)
        found = True
        break

if not found:
    print("No Saddle Point found")
