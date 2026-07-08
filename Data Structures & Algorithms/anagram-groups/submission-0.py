class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        store = {}

        for element in strs:
            count = [0] * 26
            for i in range(len(element)):                
                count[ord(element[i]) - ord("a")] += 1
            
            if (tuple(count) not in store):
                store[tuple(count)] = [element]
            else:
                store[tuple(count)].append(element)
        
        
        answer = []
        for value in store.values():
            answer.append(value)

        return answer
        


        



        
