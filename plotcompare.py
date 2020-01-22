import numpy as np
import matplotlib.pyplot as plt
import time

def usingLoops(a,b,j):
    multiplication = np.random.rand(j,j)
    start = time.time()
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                multiplication[i][j] += a[i][k]*b[k][j]
    
    timeTaken = time.time() - start
    print(timeTaken, multiplication)

    return timeTaken

def usingNumpy(a,b):
    c = time.time()
    print(a.dot(b))
    timeTaken2 = time.time() - c

    return timeTaken2

def plot(D):
    plt.bar(range(len(D)), list(D.values()), align='center')
    plt.xticks(range(len(D)), list(D.keys()))
    plt.show()

if __name__ == "__main__":
    val1 = {100:0,200:0,400:0}
    val2 = {100:0,200:0,400:0}
    
    firstMatrix = np.random.rand(100,100)
    secondMatrix = np.random.rand(200,200)
    thirdMatrix = np.random.rand(400,400)
    
    li = [firstMatrix, secondMatrix, thirdMatrix]
    j = 100

    for i in li:
        val1[j] = usingLoops(i,i,j)
        val2[j] = usingNumpy(i,i)
        j *=2

    print(val1, val2)

    sizes = [100,200,400]
    for j in sizes:
        val1[j] = val1[j]*1000
        val2[j] = val2[j]*1000

    print(val1, val2)

    plot(val1)
    plot(val2)