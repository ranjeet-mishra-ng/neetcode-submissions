class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        count = {}
        res = 0
        count[0] = 1

        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in count:
                res += count[sum-k]
            
            count[sum] = count.get(sum, 0) + 1
        
        return res