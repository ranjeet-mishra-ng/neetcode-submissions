class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for bar1 in range(len(heights)):
            for bar2 in range(bar1 + 1, len(heights)):
                area = min(heights[bar1], heights[bar2]) * (bar2 - bar1)
                max_area = max(area, max_area)
        

        return max_area