class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        res = [0] * len(nums)

        pref = 1
        for i in range(len(nums)):
            pre[i] = pref
            pref = pref * nums[i]
        
        postf = 1
        for i in range(len(nums)-1, -1, -1):
            post[i] = postf
            postf = postf * nums[i]
        

        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        
        return res
        

        