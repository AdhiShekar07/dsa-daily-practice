"""
Problem: Merge Intervals
Platform: LeetCode
Difficulty: Medium
Approach: Sorting + Interval Merging
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def merge(self, intervals):
        
        if not intervals:
            return []
        
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            
            # If overlapping
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        
        return merged
