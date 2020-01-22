import numpy as np
import time

def usingLoops(a,b,multiplication):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                multiplication[i][j] += a[i][k]*b[k][j]

    return multiplication

def usingNumpy(a,b):
    a = np.array(a)
    b = np.array(b)
    c = time.time()
    d = a.dot(b)
    timeTaken2 = time.time() - c
    return d,timeTaken2

if __name__ == "__main__":
    firstMatrix =   [[1,2,3],
                    [4,5,6],
                    [7,8,9]]
    
    secondMatrix =  [[10,11,12],
                    [13,14,15],
                    [16,17,18]]

    multipliedMatrix = [[0,0,0],
                        [0,0,0],
                        [0,0,0]]
    
    print("Using Loops:\n ")
    a = time.time()
    print(usingLoops(firstMatrix, secondMatrix, multipliedMatrix),"\n")
    timeTaken = time.time() - a
    print(timeTaken, "\n")
    
    print("Using Numpy:\n ")
    multi, timeTaken2 = usingNumpy(firstMatrix, secondMatrix)
    print(multi)
    print("\n", timeTaken2, "\n")

    if timeTaken > timeTaken2:
        print("*** Numpy was faster by: ***\n\n", timeTaken - timeTaken2)

    else:
        print("*** Loops were faster by: ***\n\n", timeTaken2 - timeTaken)