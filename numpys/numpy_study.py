import numpy as np
A= np.array([
    [1,2,3],
    [2,3,4],
    [4,5,6]
    ])

print A[0,:] # this is [1,2,3]
print A[0]
print A[:,0]

print A[1:,0]
print "the rows%s and cols%s" % A.shape


print "the result of the np.arange(0,1,0.0):" , np.arange(0,1,0.1)  # parameters(start,end,step)
#answer: [0,0.1 ... 1]

'''
M[i,j] to access the item in the ith row and j-th column
M[i:j,:]  this is to get the all the rows between the i-th and j-th;
M[:,i] to get the i-th column of M.
'''
