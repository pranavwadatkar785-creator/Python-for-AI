import numpy as np  # noqa: I001
list1= [1,2,3,4] 
arr1 = np.array(list1) 
print(type(arr1)) 
arr2d = np.array([list1,list1]) 
print(arr2d,arr2d.ndim) 
arr2d = np.array([[list1,list1,list1]]) 
print(arr2d,arr2d.ndim) 
#basic functionc in numpy 
arr1 = np.array([[[1,2,3,4],[5,6,7,8],[1, 2, 3, 4]],[[1,2,3,4],[5,6,7,8],[1, 2, 3, 4]]]) 
print(arr1) 
print("n_dim",arr1.ndim) 
print("shape",arr1.shape) 
print("size",arr1.size) 
print("dtype",arr1.dtype) 
# array initialization 
# zero array 
zer0_arr = np.zeros((1,2,3)) 
print("Zero array\n",zer0_arr) 
# one array 
one_arr = np.ones((3,2)) 
print("one array\n",one_arr) 
# Full array 
full_arr = np.full((1,2,3),15) 
print("Full array\n",full_arr) 
# identity matrix 
id_arr = np.eye(3) 
print("Identity matrix\n",id_arr) 
print(np.empty((4,2))) 
print(np.arange(0,21,3)) 
print(np.linspace(0,20,6)) 
print(np.random.rand(2,3)) 
print(np.random.randint(1,100,(3,3))) 
# array indexing and slicing 
a = np.arange(1,10,2) 
print(a) 
#slicing 
print(a[0:3:1]) 
two_D = np.array([[1,2,3],[4,5,6]]) 
print(two_D[0][1]) 
print(two_D[1]) 
print(two_D[1:]) 
#reshapeing and flattening 
list1= [1,2,3,4] 
list2= [5,6,7,8] 
arr1 = np.array([list1,list2]) 
arr1.reshape(4,2) 
arr1.reshape(8) 
arr1.reshape([2,2,2]) 
arr1.flatten() 
#vertical and horizontal stacking 
a = np.array([1,2,3,4]) 
b = np.array([5,6,7,8]) 
print(np.vstack((a,b))) 
print(np.hstack((a,b))) 
# Basic arithmetic operations 
print(np.add(a,b)) 
print(np.subtract(a,b)) 
print(np.multiply(a,b)) 
print(np.divide(a,b)) 
#dot product 
print(np.dot(a,b)) 
#Transpose 
arr1 = np.array([[1,2,3],[4,5,6]]) 
print(arr1.T) 
#statistics 
arr1 = np.array([[1,2,3], [4,5,6]]) 
print("sum",np.sum(arr1)) 
print("sum along axis 0",np.sum(arr1,axis=0)) 
print("sum along axis 1",np.sum(arr1,axis=1)) 
print("mean",np.mean(arr1)) 
print("median",np.median(arr1)) 
print("std",np.std(arr1)) 
print("var",np.var(arr1)) 
print("min",np.min(arr1)) 
print("max",np.max(arr1)) 
print("avg",np.average(arr1)) 
#array comparison 
a = np.array([1,2,3,4]) 
b = np.array([5,6,7,8]) 
print(a == b) 
print(np.array_equal(a,b)) 
print(a < b) 
#Broadcasting 
a = np.array([[1,2,3],[4,5,6]]) 
b = np.array([1,2,3]) 
print(a + b) 
print(a * b) 
#Handling nan 
data = np.array([[1,2,3],[4,np.nan,6],[7,8,9]]) 
print(np.nan_to_num(data)) 
#save and load 
a = np.array([[1,2,3],[4,5,6]]) 
np.save('array.npy', a) 
a = np.arange(1,26).reshape(5,5) 
print("Last row",a[4]) 
print("1st column",a[:,0])