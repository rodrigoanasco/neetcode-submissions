class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_hash = set(nums)

        temp = [0]
        for i in range(len(nums)):
            count = 0
            if (nums[i] - 1) in number_hash:
                continue
            
            count = count + 1
            current = nums[i] + 1
            while (current in number_hash):
                count += 1
                current += 1

            temp.append(count)
        
        return max(temp)



            