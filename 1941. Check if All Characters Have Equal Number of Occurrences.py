# Create an instance of the Solution class
from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        frequencies = counts.values()
        return len(set(frequencies)) == 1
# Example strings to test
solution = Solution()
s = "abacc"


result = solution.areOccurrencesEqual(s)
print(f"The characters in the string '{s}' all have the same number of occurrences: {result}")
