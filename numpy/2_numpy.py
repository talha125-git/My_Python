import numpy as np
import sys
import time

# reshape
arr11=np.arange(24).reshape(6,4)
print(arr11)
print("---------")
print(arr11[2])     #print 3nd row 
print("---------")
print(arr11[:,2])   #print 3rd col
print("---------")
print(arr11[:,1:3])   #print 2nd & 3rd col
print("---------")
print(arr11[2:4,1:3])
# Rows 4 and 5 (index 4:6) → [[16 17 18 19], [20 21 22 23]]
# Columns 2 and 3 (index 2:4) → [[18 19], [22 23]]
print(arr11[4:6, 2:4])

#iteration
# for i in arr11:
#     print(i)

#use function
for i in np.nditer(arr11):
    print(i)    #print in one line separatly


print("--------------------------------------------------------------------------------------")

#  Numpy opeartions
arrA = np.array([1,2,3,4,5,6])
arrB = np.array([4,5,6,7,8,9])
 
print("Subtract of arrays",arrA-arrB)
print("Multiply of arrays",arrA*arrB)
print("--------")
print("Array A multiply by two",arrA*2)
print(arrB>3)

print("--------------------------------------------------------------------------------------")
print("---- DOT PRODUCT ----")
arr12 = np.arange(6).reshape(2,3)
arr13 = np.arange(6,12).reshape(3,2)
print("Array 12 =>",arr12)
print("_____")
print("Array 13 =>",arr13)
print("_____")
o = arr12.dot(arr13)
print(o)

print("--------------------------------------------------------------------------------------")
print("___max , min , axis ____")
arr14 = np.array([2,3,4,5,6,7,8,9,11]).reshape(3,3)
print(arr14)
print(arr14.max())          #show max num in array
print(arr14.min())          #show man num in array
print(arr14.min(axis=0))    #show 1st row of array
print(arr14.min(axis=1))    #show 1st col of array
print(arr14.sum())          # sum all ele in array
print(arr14.sum(axis=0))    # show sum of 3 col
print("___________")
print(arr14.std())
print(np.sin(arr14))
print(np.median(arr14))
print(np.exp(arr14))

