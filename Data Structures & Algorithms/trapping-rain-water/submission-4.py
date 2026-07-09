class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_area = 0
        l = 0
        r = len(height) - 1
        i = 0

        counter = 0
        min_left = height[l]
        min_right = height[r]

        while(l <= r):
            if min_left >= min_right:
                print("Min left is greater than min right...\titeration:", counter, "\nmin_left:", min_left, "\tmin_right:", min_right, "\nsubtraction:", (min_left - height[l], "current max area:", max_area))
                print("\n")
                max_area += max(0, (min_right - height[r]))  
                if min_right < height[r]:
                    min_right = height[r]
                r -= 1
            else:
                print("Min right is greater than min left...\titeration:", counter, "\nmin_left:", min_left, "\tmin_right:", min_right, "\nsubtraction:", (min_left - height[l], "current max area:", max_area))
                print("\n")
                max_area += max(0, (min_left - height[l]))
                if min_left < height[l]:
                    min_left = height[l]
                l += 1
            counter += 1

        return max_area 


            
            