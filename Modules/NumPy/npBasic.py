# [+: Numerical Python https://github.com/numpy/numpy
import numpy as np

def Array():
  a = np.array(42)
  b = np.array([1, 2, 3, 4, 5])
  c = np.array([[1, 2, 3], [4, 5, 6]])
  d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

  e = np.array((1,2,3), ndmin=4)

  print(a.ndim, a)
  print(b.ndim, b)
  print(c.ndim, c)
  print(d.ndim, d)
  print(e.ndim, e)
  
  #Indexing
  print(a, b[-1], c[0,0], d[0,1,-1])

#Array()

def Slicing1D():  
  #Slicing  [start:end:step], Step is optional
  #Slicing 1 D
  x = np.array((0,1,2,3,4,5,6,7,8))
  
  print(x[1:3]) # 1,2 Including start index, excluding end index
  print(x[2:7:2]) # 2,4,6 
  print(x[-1]) # 8
  print(x[-1:1]) #[] # end must be grater than start index
  print(x[0:-1:3]) #0,3,6
  print(x[-3:]) # 6,7,8
  print(x[:3]) #0,1,2
  print(x[::2]) #0,2,4,6,8
   
#Slicing1D()

def SlicingND():
  x = np.array([[0,1, 2, 3, 4], [5, 6, 7, 8, 9]])
  print(x)
  print(x[0]) 
  print(x[0,:])
  print(x[0,0])
  print(x[0, 1:3])
  print(x[-1, -3:])
  
#SlicingND()

def DataTypes():
  pass #start here https://www.w3schools.com/python/numpy/numpy_data_types.asp

DataTypes()

