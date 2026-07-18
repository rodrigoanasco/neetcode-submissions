class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heightss = heights
        heightss.append(0)
        class box:
            def __init__(self, h: int, i: int):
                self.h = h
                self.i = i

            def __repr__(self):
                return f"(New Box, height: {self.h}, index: {self.i})"
        
        def area(hei: int, wid: int):
            return hei * wid

        box_stack = []
        
        max_area = 0
        
        for i in range(len(heightss)):
            temp = box(heightss[i], i)

            if len(box_stack) == 0:
                box_stack.append(temp)

            while len(box_stack) != 0 and (box_stack[-1].h >= temp.h):
                    temp.i = box_stack[-1].i

                    temp_area = area(box_stack[-1].h, (i - box_stack[-1].i))
                    if max_area < temp_area:
                        max_area = temp_area
                    box_stack.pop()

            box_stack.append(temp)
            
            if box_stack[-1].h < temp.h:
                box_stack.append(temp)
                
        return max_area