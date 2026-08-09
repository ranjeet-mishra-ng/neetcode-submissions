class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max_height = [-1] * n
        right_max_height = [-1] * n

        left_max_height[0] = 0

        

        for i in range(1, n):
            left_max_height[i] = max(left_max_height[i-1], height[i-1])

        right_max_height[n-1] = 0
        for i in range(n-2, -1, -1):
            right_max_height[i] = max(right_max_height[i+1], height[i+1])
        trapped_water = 0
        for i in range(0, n):
            water = min(left_max_height[i], right_max_height[i]) - height[i]
            if water > 0:
                trapped_water += water
        
        return trapped_water
        