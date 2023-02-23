#Universal Functions" are NumPy functions that operate on the ndarray object.
import numpy as np

def uFuncEx1():
  # Add 2 lists
  x = [1, 2, 3, 4]
  y = [4, 5, 6, 7]
  z = []

  for i in range(len(x)):
    z.append(x[i]+y[i])
  #OR
  z = []
  for i, j in zip(x, y):
    z.append(i - j)
  #OR
  z = np.add(x,y)
  #OR
  myMul = lambda a,b : a*b
  ufmyMul = np.frompyfunc(myMul, 2, 1) # func, nr of arrays input, nr of arrays output
  z = ufmyMul(x,y)
  print(z)

#uFuncEx1()

def Arithmatic():
  x = [10, 2, 13, 4]
  y = [4, 5, 6, 7]

  print('Add: ', np.add(x,y))
  print('Subtract: ', np.subtract(x,y))
  print('Multiply: ', np.multiply(x,y))
  print('Divide: ', np.divide(x,y))
  q,r = np.divmod(x,y)
  print('Divide(divmode, only div): ', q)
  print('Mod (div,od): ', r)
  print('DivMod: ', np.divmod(x,y))
  print('mod: ', np.mod(x,y))
  print('Power: ', np.power(x,y))
  print('ABS-Subtract: ', np.abs(np.subtract(x,y)))

#Arithmatic()

def RoudingDecimal():
  print(np.trunc([-3.1666, 3.6667]))
  print(np.fix([-3.1666, 3.6667]))
  print(np.around([-3.1666, 3.6667]))
  print(np.around([-3.1666, 3.6667],2))
  print(np.floor([-3.1666, 3.6667]))
  print(np.ceil([-3.1666, 3.6667]))

RoudingDecimal()

#log sum/cumsum, sum-axis, prod, diff, diff/n
#lcm, lcm.reduce(arr), gcd, gcd.reduce(arr)
#sin, cos, tan, deg2rad, rad2deg, inverse (arcsin, arccos, arctan), hypot() -Hypotenues
#sinh(), cosh() and tanh() hyperbolic, inverse (arcsinh, arccosh, arctanh).
#NumPy Set Operations  https://www.w3schools.com/python/numpy/numpy_ufunc_set_operations.asp

