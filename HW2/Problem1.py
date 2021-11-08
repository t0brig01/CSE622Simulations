import numpy as np 
import matplotlib.pyplot as plt

N = 100

uniform = np.random.uniform(0,1000,N)
piArray = []

def circleArea(r):
    return np.pi*(r**2)

def boundingSquareArea(r):
    return (2*r)**2

def findPi(r):
    return 4*circleArea(r)/boundingSquareArea(r)

for i in uniform:
    piArray.append(findPi(i))

for i, j in zip(uniform,piArray):
    print("num:{0} \t\t pi:{1}".format(i,j))

plt.style.use('ggplot')
plt.hist(uniform,color="#325aa8")
plt.show()

