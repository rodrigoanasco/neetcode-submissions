class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash = {}
        for element in nums:
            if element in nums_hash:
                nums_hash[element] += 1
            else:
                nums_hash[element] = 1

        for element in nums:
            if nums_hash[element] > 1:
                return True
        return False
