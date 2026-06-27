class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             return True
        
        # return False
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                j = seen[nums[i]]
                if abs(i-j) <= k:
                    return True
                
            seen[nums[i]] = i
        return False



        