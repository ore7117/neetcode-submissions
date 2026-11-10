class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # -4,-1,-1,0,1,2
        # sorted so we can run two pointers(sorted) on l = i+1, r = len(s)-1

        nums.sort()
        res = set()

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1

            while l<r:

                if nums[i]+nums[l]+nums[r] > 0:
                    r-=1 
                elif nums[i]+nums[l]+nums[r] < 0:
                    l+=1
                
                else:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
            
        
        return list(res)