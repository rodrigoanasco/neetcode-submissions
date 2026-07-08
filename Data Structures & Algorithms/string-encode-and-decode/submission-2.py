class Solution:
    def encode(self, strs: List[str]) -> str:
        code = ""
        for element in strs:
            code += str(len(element))
            code += " "
            code += element
            
        
        print(code)
        return code
        
        


    def decode(self, s: str) -> List[str]:
        answer = []
        
        num = 0
        i = 0
        while i < len(s):
            j = i
            while s[j] != " ":
                j += 1

            num = int(s[i:j])
            
            i = j + 1
            j = i + num

            answer.append(s[i:j])

            i = j
        
        return(answer)
             
            


    
