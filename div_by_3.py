# NUMPY PROBLEM # 2
import numpy as np 
x= np.arange(1,101,1).reshape(10,10)
y=x*x
z=y%3
Div_by_3 =y[z == 0]
np.save('div_by_3.npy',Div_by_3)

print('Matrix Square 10x10 =')
print (y)
print('Numbers That are  Divisible by 3 in the Matrix Square 10x10:')
print(Div_by_3)
