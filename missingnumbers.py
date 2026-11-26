class Solution:
     def missingnumber(self,nums: list[int])->int:
            n=len(nums)
            r_sum=n*(n+1)//2
            l_sum=sum(nums)
            return r_sum-l_sum