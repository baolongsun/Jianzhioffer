height = [4,5,1,5,5]
add_height = 3
while add_height:
    height = sorted(height)
    height[0] += 1
    add_height -= 1
print(height[0])
