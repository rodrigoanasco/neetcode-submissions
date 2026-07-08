class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        answer = []

        for i in range(len(nums)):
            
            if nums[i] in sums:
                answer.append(sums[nums[i]])
                answer.append(i)
                return answer
            
            else:
                sums[target - nums[i]] = i