class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict =  {}
        for i in range (len(nums)):
            num = nums[i]
            comp = target - num
            if comp in dict:
                return [i, dict[comp]]
            
            dict[num] = i
        return [-1, -1]        


## this is to check the solution
solution = Solution()
nums = [2,7,11,15]
target = 9

result = solution.twoSum(nums, target)
print(result)

"""Step-by-Step Process:
Initialization: A dictionary (often referred to as a hashmap) is initialized to keep track of the numbers and their corresponding indices as they are processed.

Input Values:

nums = [2, 7, 11, 15]
target = 9
Loop Execution:
Initialization: dict = {}

Iteration 0:
i = 0, num = 2
comp = 9 - 2 = 7 (complement needed to reach the target)
dict does not contain 7, so:
Add 2 with its index to dict: dict = {2: 0}

#Iteration 1:
i = 1, num = 7
comp = 9 - 7 = 2 (complement needed to reach the target)
dict contains 2 This is because 2 was added during iteration 0.
dict[2] returns index 0.
Return: [1, 0] because nums[1] + nums[0] = 7 + 2 = 9, which is the target.

Explanation of Output:
The function would return [1, 0], indicating the indices of the numbers in the list that sum up to the target of 9. 
The indices 1 and 0 correspond to the numbers 7 and 2, respectively. 
Here's how the final output is derived:

The numbers at indices 1 and 0 are 7 and 2. Adding these gives 7 + 2 = 9, which matches the target.
Conclusion:
This demonstrates how the twoSum function effectively uses a dictionary to track previously encountered numbers and their indices to quickly find a pair that sums to a given target. 
This approach avoids the need for a nested loop, thus operating in linear time 
𝑂(𝑛), where 𝑛 is the length of the list nums. The example shows that the function correctly identifies the two numbers 7 and 2 from the list that add up to the target 9."""