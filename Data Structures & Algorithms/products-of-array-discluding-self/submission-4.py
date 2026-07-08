class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        #Loop to build prefix
        initial_prefix = 1
        for i in range(len(nums)):
            output.append(initial_prefix)
            initial_prefix = initial_prefix * nums[i]
        print(output)
        
        #Loop to build sulfix
        initial_sulfix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] = output[j] * initial_sulfix
            initial_sulfix *= nums[j]
        
        return(output)
        
            