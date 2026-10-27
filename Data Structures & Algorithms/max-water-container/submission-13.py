class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len(heights)-1
        maxArea = 0


        while l<r:
            height = min(heights[r],heights[l])
            width = (r-l)
            area = width * height

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1 
            
            maxArea = max(area,maxArea)
        
        return maxArea 