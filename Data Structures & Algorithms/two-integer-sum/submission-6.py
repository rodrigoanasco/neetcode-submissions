class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         temp = {}
         for i in range(len(nums)):
            if nums[i] not in temp:
                temp[target - nums[i]] = i
            else:
                return [min(temp[nums[i]], i), max(temp[nums[i]], i)]