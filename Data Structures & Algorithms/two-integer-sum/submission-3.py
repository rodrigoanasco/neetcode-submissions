class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_track = {}
        
        answer = []

        for i in range(len(nums)):
            num_track[nums[i]] = i
        
        for j in range(len(nums)):
            temp = target - nums[j]
            if (temp in num_track):
                if (j != num_track[temp]):
                    answer.append(j)
                    answer.append(num_track[temp])
                    break

        return answer