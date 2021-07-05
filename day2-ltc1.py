class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      res = {}
      # Assigns a index value to each value in the array
      for i, num in enumerate(nums):
        # If you find the number that would sum to target
        if target - num in res:
          # return the indices
          return [res[target-num], i]
        # Else, put the new number in the results dict
        res[num] = i
