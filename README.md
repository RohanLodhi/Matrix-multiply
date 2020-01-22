# Matrix-multiply
For GCI 2019, multiplication of matrices using loops vs numpy.

# Python Loop code used:
```

for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                multiplication[i][j] += a[i][k]*b[k][j]
    
```
# Following are the main reasons behind the fast speed of Numpy:
Numpy array is a collection of similar data-types which are densely packed in memory. A Python list can have different data-types, which puts lots of extra constraints while doing computation on it.
Numpy is able to divide a task into multiple subtasks and process them parallelly.
Numpy functions are implemented in C. Which again makes it faster compared to Python Lists.

# Reasons behind NumPy's faster matrix multiplication:
The dot product is one of the most important and frequent operations in Machine Learning algorithms. Especially in Neural Networks training, where we need to do a lot of Matrix Multiplication.
Let's compare the speed of the dot product now.

![Image 1](https://miro.medium.com/max/1578/1*X8ihnYLDSRryF7yOKiXb4A.png)
![Image 2](https://miro.medium.com/max/1591/1*HkeEOsLd32hozdNyH7oWbw.png)

Numpy is around 10 times faster. Let’s plot the speed for different array sizes.

![Image 3](https://miro.medium.com/max/1134/1*mw7cUXtY_YId3QHTSucyew.png)

We see that dot product is even faster. Which is around 140 times fast as we move to the large array size.
