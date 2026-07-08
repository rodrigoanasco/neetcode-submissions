class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_1 = {}
        hash_2 = {}

        for i in range(len(s)):
            if s[i] not in hash_1:
                hash_1[s[i]] = 1
            else:
                hash_1[s[i]] = hash_1[s[i]] + 1
        
        for i in range(len(t)):
            if t[i] not in hash_2:
                hash_2[t[i]] = 1
            else:
                hash_2[t[i]] = hash_2[t[i]] + 1
        
        print(hash_1)
        print(hash_2)

        if hash_1 == hash_2:
            return True
        else:
            return False
        

            
        
        