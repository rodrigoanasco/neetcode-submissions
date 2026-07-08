class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for element in strs:
            answer += str(len(element))
            answer += "%"
            answer += element
        print(answer)
        return answer


    def decode(self, s: str) -> List[str]:
        
        answer = []
        if s == "":
            return answer
        
        n = 0
        while True:
            temp = ""
            # Set up the key
            while(s[n] != "%"):
                temp += s[n]
                n += 1
    
            key = int(temp)
            
            temp = ""
            n += 1
            for i in range(key):
                temp += s[n + i]
            answer.append(temp)
            
            print(answer)
            n += key

            if n == len(s):
                break
        
        return answer
