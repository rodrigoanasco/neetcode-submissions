class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        class temp_cord:
            def __init__(self, temp, index):
                self.temp = temp
                self.index = index
            
            # Esto le enseña a Python cómo imprimirse de forma bonita
            def __repr__(self):
                return f"temp_cord(temp={self.temp}, index={self.index})"

        maximum = []
        initial = temp_cord(temperatures[-1], len(temperatures) - 1)
        maximum.append(initial)

        
        ans = []
        ans.append(0)
        for i in range(len(temperatures) - 2, -1, -1):
            print("Iteration:", len(temperatures) - i - 1, "number of elements in maximum:", len(maximum))
            print("Current element:", temperatures[i],"\n")
            while len(maximum) != 0:
                if maximum[-1].temp > temperatures[i]:
                    print("Entering FIRST CONDITIONAL \ncurrent element:", temperatures[i], "current max:", maximum[-1].temp)
                    ans.append(maximum[-1].index - i)
                    print("Appended maximum[-1].index - i to ANS, current ans:", ans)
                    maximum.append(temp_cord(temperatures[i], i))
                    print("Appended to MAXMIUM, now maximum is:", maximum, "EXITING FIRST CONDITION\n")
                    break
                
                elif maximum[-1].temp <= temperatures[i]:
                    print("ENTERING SECOND CONDITION, POPPING MAXIMUM")
                    maximum.pop()
                    print("CURRNET MAXIMUM:", maximum, "EXITING SECOND CONDITION\n")
            
            if len(maximum) <= 0:
                    maximum.append(temp_cord(temperatures[i], i))
                    ans.append(0)
        
        ans.reverse()
        print("final answer:", ans)
        return ans
                        
                        
            