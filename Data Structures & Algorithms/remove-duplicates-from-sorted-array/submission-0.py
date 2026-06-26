class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        res = 1

        for i in range(len(nums)):
            if nums[i] != nums[res - 1]:
                nums[res] = nums[i]
                res += 1
        
        return res

        