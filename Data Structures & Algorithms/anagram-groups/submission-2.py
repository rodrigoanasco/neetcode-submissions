class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use an array as a hash map key
        # Use a hash map to locate how many of the anagrams there are
        # Populate the hashmap with a list and then append any additional word

        temp = {}
        for i in range(len(strs)):
            bit = [0] * 26
            for j in range(len(strs[i])):
                index = ord(strs[i][j]) - ord('a')
                bit[index] += 1

            temp2 = tuple(bit)
            if temp2 in temp:
                temp[temp2].append(strs[i])
            else:
                temp[temp2] = [strs[i]]

        result = []
        for element in temp.values():
            result.append(element)
        
        return result