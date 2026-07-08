class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        l_max = heights[left]
        r_max = heights[right]

        area = 0
        
        iteration = 0
        while(left < right):
            print("iteration: ", iteration)
            
            if area < (right - left) * min(l_max, r_max):
                area = (right - left) * min(l_max, r_max)
                print("area: ", area)
            

            print("lmax: ", l_max, "rmax: ", r_max)
            if l_max < r_max:
                left += 1
                l_max = heights[left]
                print("increase left by one, now is: ", right)
            elif r_max <= l_max:
                right -= 1
                r_max = heights[right]
                print("decrease right by one, now is: ", left)
            
            iteration += 1

            print("Current area: ", area)
            print(" ")
        return area
