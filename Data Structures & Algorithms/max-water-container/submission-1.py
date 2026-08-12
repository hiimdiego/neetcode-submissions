class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Initialize pointers and max area
        l, r = 0, len(heights) - 1
        max_area = 0
        #While loop
        while l < r:
            #Initialize width and height
            width = r - l
            height = min(heights[l], heights[r])
            #Update max_area if necessary
            if (height * width > max_area):
                max_area = height * width
            #Update ptr depending on whether left or right is bigger
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        return max_area