class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for element in nums:
            if element not in map:
                map[element] = 1
            else:
                return True

        return False