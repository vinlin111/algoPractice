def maxArea(height):
    area = 0
    top = len(height) - 1
    bottom = 0
    while top > bottom:
            
        a = min(height[bottom], height[top]) * (top-bottom)
        if a > area:
            area = a
            
        if height[bottom] > height[top]:
            top-=1
        elif height[bottom] < height[top]:
            bottom+=1
        else:
            top-=1
            bottom+=1
    return area

print(maxArea([1,8,6,2,5,4,8,3,7]))