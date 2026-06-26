class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        

        pairs = list(count.items())
        sorted_pairs = sorted(pairs, key = lambda item: item[1], reverse = True)
        res = []

        for i in range(k):
            if i == len(nums):
                return res
            
            res.append(sorted_pairs[i][0])
        
        return res

        
        