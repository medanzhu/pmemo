array = []
 
array.append(1)
array.append(2)
array.append(3)
array.append(4)
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

#获取数组里某个值
item = array[0]
 
# Use the array like a stack.  Note that using the pop() method removes the element.
#array.pop()  # Pop last item in a list
#array.pop(0) # Pop first item in a list
 
#获取数组里最后一个值
item = array[-1] # Retrieve last element in a list.

#超出边界会报错
try:
    # This will cause an exception, which will then be caught.
    print(array[len(array)])
except IndexError as e:
    # Print the exception. 
    print(e)