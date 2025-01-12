# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

class Solution:
  def missnum(self, nums):
      n = len(nums)
      sum_n = n * (n+1) // 2
      sum_nums= sum(nums)
      return sum_n - sum_nums

solution = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(solution.missnum(nums))
    