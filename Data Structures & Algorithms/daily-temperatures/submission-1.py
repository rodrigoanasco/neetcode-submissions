class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        class temp_cord:
            def __init__(self, temp, index):
                self.temp = temp
                self.index = index

        maximum = []
        initial = temp_cord(temperatures[-1], len(temperatures) - 1)
        maximum.append(initial)

        
        ans = []
        ans.append(0)
        for i in range(len(temperatures) - 2, -1, -1):
            while len(maximum) != 0:
                if maximum[-1].temp > temperatures[i]:
                    ans.append(maximum[-1].index - i)
                    maximum.append(temp_cord(temperatures[i], i))
                    break
                
                elif maximum[-1].temp <= temperatures[i]:
                    maximum.pop()
                    
            if len(maximum) <= 0:
                    maximum.append(temp_cord(temperatures[i], i))
                    ans.append(0)
        
        ans.reverse()
        return ans
                        
                        
            