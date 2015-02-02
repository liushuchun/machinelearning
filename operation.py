import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0, 4 * np.pi, 1000)
C = np.cos(X)
S = np.sin(X)

#plt.plot(X, C)
#plt.plot(X, S)

A = np.arange(100)
print np.mean(A)
print A.mean()

C = np.cos(A)
print C.ptp()

#--------------------basic operation--------------
a = np.array([10, 30, 40, 40])
b = np.arange(4)
print 'a:', a
print 'b:', b
print 'a+b:', a + b
print 'a-b:', a - b

A = np.array([
    [1, 2],
    [3, 4]
])
B=np.array([
    [0,1],
    [2,3]])
print 'A*B(multi one by one):',A*B
print 'np.dot(A,B) the real A*B:',np.dot(A,B)

#the += & *= will update the matrix right now
a = np.ones((2,3), dtype=int)
b=np.random.random((2,3))
a*=3
print "a now:",a
b+=a
print ""


