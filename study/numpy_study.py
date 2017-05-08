# coding: utf-8
import numpy as np

# ndarray是通用多纬容器
# 每个数组有个shape(各维度大小),dtype(对象类型)

# 1创建数组
data1 = [6, 6.5, 8, 0, 1]
data = np.array(data1)

print data

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

print "np.array(data2)"
arr2 = np.array(data2)

print "arr2.ndim"
print arr2.ndim

print "arr2.shape"
print arr2.shape

print "np.zeros(10)"
print np.zeros(10)

print "np.zeros((3,6))"
print np.zeros((3, 6))

print "np.empty((2,3,2))"
print np.empty((2, 3, 2))

# 数组和标量之间的运算

arr = np.array([[1., 2., 3.], [4.0, 5., 6.]])
print arr

print "arr * arr", arr * arr

print "1/arr", 1 / arr

# 不同大小的数组之间的运算叫broadcasting

print "np.arange(10)", np.arange(10)

arr[5:8] = 12
print "arr[5:8]", arr


# sqrt(arr)

print "np.sqrt(arr)", np.sqrt(arr)

print "np,exp(arr)", np.exp(arr)

print "np.add(arr,arr)", np.add(arr, arr)

print "np.maximum(arr,arr)", np.maximum(arr, arr)

'''
一元
abs,fabs,

sqrt平方根
squre 平方
exp 指数e(x)
log,log10,log2,log1p

sign

ceil celing值

floor 地板值
rint 四舍五入

modf 数组的小数和整数部分以独立的形式返回

cos,cosh,sin,sinh

tan,tanh


二元

add
substract
multiply 相乘
divide除法，floor_divide 向下整除法
power A的B次方

maximum,fmax fmax忽略NAN
minmum,fmin一样
mod 求莫
greater,greater_equal
less,less_equal
equal,not_equal

'''

# 数学和统计方法sum,mean,
arr = np.random.randn(5, 4)
print arr.mean()

print np.mean(arr)

print "arr.sum():", arr.sum()

# 还可以添加axis
print arr.mean(axis=1)

print arr.sum(0)

# 排序
print "pre arr", arr
print "post sort arr", arr.sort()

# 矩阵运算

x = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
y = np.array([[6.0, 23.0], [-1, 7], [8, 9]])

print "x*y",  # x * y #error
print "np.dot(x,y)", x.dot(y)


'''
常用的线性函数
diag 一维数组的形式返回方阵的对角线元素，或将一维数组返回反阵
dot 矩阵乘法
trace 对焦元素的和
det 行列式
eig 计算方阵的特征值和特征向量
inv 矩阵的逆矩阵
pinv 矩阵的Moore-Penrose伪
qr qr分解
svd 奇异值分解
solv AX=B 解
lstsq Ax=b最小二乘
'''

# 随机数生成

# 生成标准正态分布4X4矩阵
sample = np.random.normal(size=(4, 4))

'''
seed
permutation
shuffle
rand
randint
randn
binomial
normal
beta
chisquare
gamma
uniform

'''
