class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # 2p approach

        # left pointer at beginning, right starts at maximum width
        # since we are looking for the best comnination of height and width, if heights[l]<heights[r], move l forward. l is a bottleneck
        # if heights[l] is greater than right, right is a bottleneck. move right backwards
        # constatly calculate the area 
        l = 0 
        r = len(heights)-1
        maxArea = 0 
        

        while l < r: 
            height = min(heights[l],heights[r])
            width = r - l 
            area = height * width 
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

            maxArea = max(area,maxArea)
        
        return maxArea 
