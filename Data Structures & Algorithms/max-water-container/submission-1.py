class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        # for bar1 in range(len(heights)):
        #     for bar2 in range(bar1 + 1, len(heights)):
        #         area = min(heights[bar1], heights[bar2]) * (bar2 - bar1)
        #         max_area = max(area, max_area)
        

        # return max_area

        left = 0
        right = len(heights) - 1

        while left < right:
            h = min(heights[left], heights[right])
            w = right - left

            area = h * w
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area