# 11. Container With Most Water
# link : https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    n = len(height)
    maxArea = 0
    for i in range(n):
        left = i
        right = n-i-1

        if(left > right):
            break
        
        target = height[left] if height[left] < height[right] else height[right]
        
        area = target * (right - left)

        if area > maxArea:
            maxArea = area

    return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))
# print()
