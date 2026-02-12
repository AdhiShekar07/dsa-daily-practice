"""
Problem: Find Equilibrium Index in an Array
Platform: GeeksforGeeks
Difficulty: Easy
Approach: Prefix Sum Technique
Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = list(map(int, input("Enter elements: ").split()))

total_sum = sum(arr)
left_sum = 0

for i in range(len(arr)):
    right_sum = total_sum - left_sum - arr[i]
    
    if left_sum == right_sum:
        print("Equilibrium Index:", i)
        break
    
    left_sum += arr[i]
else:
    print("Equilibrium Index: -1")
