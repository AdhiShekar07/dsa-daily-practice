"""
Problem: Minimum Deletions to Make Two Strings Equal
Platform: LeetCode
Difficulty: Medium
Approach: Dynamic Programming (LCS)
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

m = len(s1)
n = len(s2)

# Step 1: Create DP table
dp = [[0] * (n + 1) for _ in range(m + 1)]

# Step 2: Fill DP table for LCS
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# Step 3: Length of LCS
lcs_length = dp[m][n]

# Step 4: Minimum deletions
min_deletions = (m - lcs_length) + (n - lcs_length)

print("Minimum deletions required:", min_deletions)
