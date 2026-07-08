class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = []
        anagrams = defaultdict(list)


        for element in strs:

            temp = [0] * 26
            

            for c in range(len(element)):
                temp[ord(element[c]) - ord('a')] += 1
            anagrams[tuple(temp)].append(element)
        
        for v in anagrams.values():
            answer.append(v)
        
        return answer