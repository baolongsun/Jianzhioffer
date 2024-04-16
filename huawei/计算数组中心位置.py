array = [2,5,3,6,5,6]
array.insert(0,1)
array.append(1)

right = 1
for i in array:
    right *= i

left = 1
for i in range(1,len(array)-1):
    left = left * array[i-1]
    right = right // array[i]
    if left == right:
        print(i-1)
        break