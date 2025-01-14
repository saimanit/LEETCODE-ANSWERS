from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
        


solution = Solution()
# Example list of strings
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Create an instance of the Solution class


# Call the groupAnagrams method and store the result
result = solution.groupAnagrams(strs)

# Print the result
print(result)