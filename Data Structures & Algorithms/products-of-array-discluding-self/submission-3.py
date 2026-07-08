class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        total = 1
        thereis = False
        all_zero = 0
        for element in nums:
            if element == 0:
                thereis = True
                all_zero += 1
            elif element != 0:
                total *= element

        if all_zero > 1:
            return [0] * len(nums)
        for element in nums:
            
            if thereis == True and element != 0:
                output.append(0)
            elif element != 0:
                temp = int(total / element)
                output.append(temp)
            else:
                temp = total
                output.append(temp)
            
        
        return output
            
            