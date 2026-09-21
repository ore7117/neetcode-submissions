class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # key = i , value = everything except i 
        # return an array of the product each value in the dictionary   
        output = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j: 
                    continue
                product *= nums[j]
            
            output.append(product)

        return output 