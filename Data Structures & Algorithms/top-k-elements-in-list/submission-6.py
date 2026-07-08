class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # The quantity does matter so we need to use a map
        temp = {}
        for element in nums:
            if element not in temp:
                temp[element] = 1
            else:
                temp[element] += 1
        
        answer = []
        for i in range(k):
            temps = max(temp, key=temp.get)
            answer.append(temps)
            temp.pop(temps)

        
        print(answer)
        return answer
        

