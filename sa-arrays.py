array = []
 
array.append(1)
array.append(3)
array[0] = 2
 
print(array)
size = 3
#如果需要，可以初始化一个数组
myArray = [0] * size
print(myArray)
#初始化一个二维数组
width  = 3
height = 4
myArray2 = [[0 for x in range(width)] for y in range(height)]
print(myArray2)