class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_area = 0
        
        i = 0
        k = 0
        temp = 0
        while(k < len(height)):
            left = height[i]
            right = height[k]
            
            
            if left > right:
                temp += (left - right)            
            
            elif left <= right:
                max_area += temp
                temp = 0
                #index of left must be the same one as right
                i = k
            k += 1
            
            
        print("final i:", i)
        print("final k:", k)


        temp = 0
        k -= 1
        r = len(height) - 1
        while(i <= k):
            print("i is:", i, "k is:", k)
            
            right = height[r]
            left = height[k]

            if (right > left):
                temp += (right - left)
                print("increasing temp, value:", temp)

            elif (right <= left):
                print("current left is:", left, "current right is:", right, "|| current index k is:", k, "current r is:", r)
                max_area += temp
                temp = 0
                r = k
            k -= 1

        return max_area
            
            