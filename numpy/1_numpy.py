# creating numpy/n-d array
import numpy as np

print("___ 1D array ___")
arr1=np.array([1,2,3,4,5])
print(arr1)
print(arr1.shape)
print(type(arr1))

print("--------------------------------------------------------------------------------------")
print("___ 2D array ___")
# 2D array
arr2= np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.shape)

print("--------------------------------------------------------------------------------------")
print("___ zeros matrox ___")
# zeros 
arr3=np.zeros((3,4))
print(arr3)
print(arr3.shape)

print("--------------------------------------------------------------------------------------")
print("___ ones matrix ___")
# ones array
arr4=np.ones((2,3))
print(arr4)
print(arr4.shape)

print("--------------------------------------------------------------------------------------")
print("___ Identity matrix ___")
# identity  (show 1 diagnal)
arr5=np.identity(4)
print(arr5)
print(arr5.shape)

print("--------------------------------------------------------------------------------------")
print("___ Arange function ___")
# arrange 
arr7a=np.arange(10)
arr7b=np.arange(10,20)
arr7c=np.arange(1,10,2)
print(arr7a)
print(arr7b)
print(arr7c)
print(arr7c.shape)

print("--------------------------------------------------------------------------------------")
print("___ linespace function ___")
# linspace
arr8=np.linspace(10,20,10)
print(arr8)
print(arr8.shape)
print("Datatype  =>",arr8.dtype)  # float64
convert_to_other_datatype = arr8.astype('int')
print(convert_to_other_datatype)

print("--------------------------------------------------------------------------------------")
print("___ 2D array with functions(shape,ndim,Size,itemsize,dtype,astype) ___")
# 2D array
arr9=np.array([[[1,2],[3,4]]     ,     [[4,6],[7,8]]])
print(arr9)
print("shape     =>",arr9.shape)
print("Dimension =>",arr9.ndim)   # show matrix  1D 2D OR 3D
print("Size      =>",arr9.size)
print("Itemsize  =>",arr9.itemsize)
print("Datatype  =>",arr9.dtype)
#astype  (to convert to another datatype)
convert_to_other_datatype = arr9.astype('float')
print(convert_to_other_datatype)

print("--------------------------------------------------------------------------------------")
print("___ List and array  ___")
# List and array
lista= range(100)
arr10=np.arange(100)
print(lista)
print(arr10)
import sys
print(sys.getsizeof(7)*len(lista))
print(arr10.itemsize*arr10.size)

print("--------------------------------------------------------------------------------------")
print("___ Time count number in how many sec or milli sec ___")
# time
import time
x=range(100000)
y=range(100000,200000)
 
start_time = time.time()
c=[(x,y) for x,y in zip(x,y)]
print(time.time()-start_time)  # count  100000 in how many sec or milli sec

a=np.arange(100000)
b=np.arange(100000,200000)
c=a+b
print(time.time()-start_time)