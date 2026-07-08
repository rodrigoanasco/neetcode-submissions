class Solution:
    def isPalindrome(self, s: str) -> bool:
        initial = 0
        print(s)
        actual = s.lower()
        actual = actual.replace(" ", "")

        final = len(actual) - 1

        print(actual)
        for i in range(len(actual) - 1):
            if initial == final:
                break

            print("initial, final loop:", i,actual[initial], actual[final])
            if (actual[initial] < "a" or actual[initial] > "z") and (actual[initial] < "0" or actual[initial] > "9"):
                print(actual[initial], "left")
                initial += 1
                continue
            if (actual[final] < "a" or actual[final] > "z") and (actual[initial] < "0" or actual[initial] > "9"):
                print(actual[final], "right")
                final -= 1
                continue

            if actual[initial] != actual[final]:
                print(actual[initial], actual[final])
                return False
            
            initial += 1
            final -= 1
            

        
        return True

            