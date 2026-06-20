class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # for i in range(0, n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [-1, -1]

        seen = {}
        for i in range(n):
            req = target - nums[i]
            if req in seen:
                return [seen[req], i]
            seen[nums[i]] = i
        return [-1, -1]
        


        