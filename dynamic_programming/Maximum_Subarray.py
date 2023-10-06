## Using Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi=nums[0]
        n=len(nums)

        for i in range(0,n):
            sum+=nums[i]

            if (sum>maxi):
                maxi=sum
            if (sum<0):
                sum=0
        return maxi


        
