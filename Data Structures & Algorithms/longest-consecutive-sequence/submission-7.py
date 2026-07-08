class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        temp = list(set(nums))
        counts = []

        for i in range(len(temp)):

            initial = temp[i]
            count = 1
            j = 1
            while(True):
                if temp[i] - j in temp:
                    count += 1
                    j += 1
                else:
                    break
            counts.append(count)

        return max(counts)