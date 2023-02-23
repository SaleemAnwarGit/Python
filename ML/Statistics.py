# Mean, Median, and Mode https://www.w3schools.com/python/python_ml_mean_median_mode.asp
# standard deviation, variance
import numpy as np
from scipy import stats
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import pandas

def Mean():
  speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
  meanSpeed  = sum(speed) / len(speed)
  print(f'Mean using logic: {meanSpeed}')
  #OR use numpy
  meanSpeed = np.mean(speed)
  print(f'Mean using np.mean: {meanSpeed}')

#Mean()

def Median():
  speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

  #use numpy
  medianSpeed = np.median(speed)
  print(f'Median using np.median: {medianSpeed}')

  #OR use logic
  speed.sort() # first sort then find middle
  medianSpeed = speed[len(speed)//2] # approximate way
  print(f'Median using logic: {medianSpeed}')
  
#Median()

# Use the SciPy mode() method to find the number that appears the most:

def Mode():
  speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
  x = stats.mode(speed)
  print(f'Mode using Scipy.mode: {x}')

#Mode()

#The Mean, Median, and Mode are techniques that are often used in Machine Learning, so it is important to understand the concept behind them.
#fgsm: fast gradian ...
# Standard deviation is spread of value represented as sigma σ
def StdDev():
  speed = [86,87,88,86,87,85,86]
  x = np.std(speed)
  print(f'Standard Deviation np.std: {x}')

#StdDev()

# σ2 sigma sqr
def Variance():
  speed = [86,87,88,86,87,85,86]
  x = np.var(speed)
  print(f'Variance np.var: {x}')

#Variance()

def Percentile():
  ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
  x = np.percentile(ages, 75)
  print(f"75th np.percentile : {x}")

#Percentile()

def Distribution():
  x = np.random.uniform(0.0, 5.0, 100)
  plt.hist(x, 5)
  plt.title('Uniform Random Distribution')
  plt.show()

  y = np.random.normal(5.0, 1.0, 100000)
  plt.hist(y, 100)
  plt.title('Normal Random Distribution')
  plt.show()

#Distribution()

def Scatter():
  x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
  y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

  slope, intercept, r, p, std_err = stats.linregress(x, y)

  def myfunc(x):
    return slope * x + intercept

  linear = list(map(myfunc, x))

  plt.scatter(x, y)
  plt.plot(x, linear)
  
  poly = np.poly1d(np.polyfit(x, y, 3))
  myline = np.linspace(1, 22, 100)

  plt.plot(myline, poly(myline))

  plt.show()

Scatter()