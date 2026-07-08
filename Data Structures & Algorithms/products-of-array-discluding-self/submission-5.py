class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Most classical way: Multiply everything and then just divide by the key
        total = 1
        zeroes = 0 #There is a single zero in the list
        for element in nums:
            if element != 0:
                total *= element
            else:
                zeroes += 1

        print(zeroes)
        answer = []

        if zeroes > 1:
            return [0] * len(nums)
        
        for element in nums:
            if element != 0 and zeroes < 1:
                answer.append(int(total / element))
            
            elif zeroes == 1:
                if element != 0:
                    answer.append(0)
                elif element == 0:
                    print(total)
                    answer.append(total)
        
        return answer