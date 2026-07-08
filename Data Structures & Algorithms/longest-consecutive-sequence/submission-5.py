class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set()
        for element in nums:
            if element not in temp:
                temp.add(element)
        
        temp2 = sorted(list(temp))
        print(temp2)

        answer = 0
        j = 0
        for i in range(len(temp2)):
            length = 1
            while(j < len(temp2) - 1):
                print("in loop", i)
                if (abs(temp2[j] + 1) == abs(temp2[j + 1])):
                    print(temp2[j] + 1)
                    print(temp2[j + 1])
                    length += 1
                    j += 1
                else:
                    break
                print(j)
            if length > answer:
                answer = length
            
            j += 1

            if j == len(temp2):
                break
        
        return answer


