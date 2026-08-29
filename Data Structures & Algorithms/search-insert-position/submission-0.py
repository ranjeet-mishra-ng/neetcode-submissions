class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        if target > nums[h]:
            return len(nums)
        
        if target < nums[l]:
            return 0
        
        ans = -1
        

        while l <= h:
            mid = l + (h - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                ans = mid
                h = mid - 1
        return ans