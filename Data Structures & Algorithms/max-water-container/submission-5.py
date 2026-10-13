class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxArea=0

        while l<r:
            height = min(heights[r],heights[l])
            width = r-l
            area=height*width

            if heights[r]<heights[l]:
                r-=1
            else:
                l+=1
            maxArea=max(maxArea,area)
        return maxArea