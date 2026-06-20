class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        k = 0

        while i <= j:

            while i < len(nums) and nums[i] != val:
                i += 1
            
            while j >= 0 and nums[j] == val:
                k += 1
                j -= 1
            
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
           
           

        return len(nums) - k

        