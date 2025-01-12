from collections import defaultdict
from typing import List 

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)  
        for arr in nums:
            for x in arr:
                counts[x] += 1 

        n = len(nums) 
        ans = []  
        for key in counts:
            if counts[key] == n:  
                ans.append(key)  

        return sorted(ans) 

# Usage:
solution = Solution()
nums = [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]
print(solution.intersection(nums))  # Expected Output: [3, 4]
