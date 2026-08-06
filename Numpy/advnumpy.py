import numpy as np  # noqa: I001
import numpy.ma as ma  # noqa: PLR0402

# broadcasting
a = np.array([1,2,3])
b = np.array([[4],[5]])

print(a + b)

# dimensional indexing
a = np.array([[[1,2,3],
               [4,5,6],
               [7,8,9]],
              [[9,8,7],
               [6,5,4],
               [3,2,1]]])
print(np.shape(a))
print('=============================')
#       F,R,C
print(a[0,2,2])
print(a[:,1,1])
print('=============================')
# newaxis
print(a[:,1,1,np.newaxis])
print('=============================')
#        Face
print(a[[0,1]])
print('=============================')
#        F    R
print(a[[1],[0,2]])
print('=============================')
#        F    Rows  Columns
print(a[[0],[0,1,2],[0,1,2]])
print('=============================')
#       Face       Row               Column
print(a[[0],[True,False,False],[False,True,True]])


# sorting and searching
a = np.array([[5,4,9],
              [1,7,3],
              [6,2,8]])

print(np.sort(np.sort(a,axis=0),axis=1))

print(np.sort(a.flatten()).reshape(a.shape))
print(a.flatten())
print(a.argmax()) #index of highest value

# iteration
a = np.array([[5,4,9],
              [1,7,3],
              [6,2,8]])
for x in np.nditer(a, order="F"): # C- for normal row wise, F- for column wise
    print(x, end=" ")
print()

with np.nditer(a, op_flags=["readwrite"]) as it:
    for element in it:
        element[...] = element**2

print(a)

# masking array import numpy.ma as ma
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
masked_arr = ma.masked_array(arr, mask=[[0,1,0],[0,0,1],[1,0,0]])
print(masked_arr)
print(masked_arr.sum())
print(ma.getmask(masked_arr))

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ma.masked_greater(arr, value=5))
print(ma.masked_less(arr, value=5))

print(ma.masked_inside(arr, v1=3, v2=7))
print(ma.masked_outside(arr, v1=3, v2=7))
print(ma.masked_where(arr % 2 !=0, arr))

#vectorization and matrix multiplication
arr = np.array([1,2,3,4,5])

def square(x):
    if x % 2 == 0:
        return x**2
    else:
        return x

vectorized_square = np.vectorize(square)
print(vectorized_square(arr))

A = np.array([[1,2],
              [4,5]])
B = np.array([[7,8],
              [10,11]])
print(np.shape(A))
print(np.shape(B))
print(np.matmul(A,B)) # or print(A @ B)


# custom data types
dt = np.dtype([('name', 'S10'), ('age', 'i4'), ('height', 'f4')])
data = np.array([('Alice', 25, 5.5), ('Bob', 30, 6.0), ('Charlie', 35, 5.8)], dtype=dt)
print(data.dtype)

