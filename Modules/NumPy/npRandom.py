#Random means something that can not be predicted logically.
from numpy import random
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

def Ex1():
  #method random gives float values between 0~1 so does the method rand
  a =random.random()  # between 0~1 
  b =random.random(size= 3)
  c =random.random(size= [2,3]) 

  d = random.rand()
  e = random.rand(2)
  #print(a,b,c,d,e)

  f = random.randint(10)
  g = random.randint(1,10)
  h = random.randint(100, size=(3, 5))
  i = random.choice([3, 5, 7, 9])
  j = random.choice([3, 5, 7, 9], size=(3, 5))
  print(f,g,h, i, j)

#Ex1()

def Distribution():
  print('Choice based on defined probabilites: ' ,x:= random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)))
  # arr = np.array([1, 2, 3, 4, 5])
  # random.shuffle(arr)
  # print(arr)
  # print(random.permutation(arr))

  sns.displot(x)  # explore seaborn
  plt.show()      # explore pyplot

  #
  x = random.normal(loc=1, scale=2, size=(2, 3))
  sns.displot(n:=random.normal(size=1000), hist=False)
  
  plt.show()

Distribution()
