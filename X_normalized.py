# NUMPY PROBLEM #1

import numpy as np 
X=np.random.random((5,5))
Y=(X-np.mean(X))/np.std(X)
np.save('X_normalized.npy',Y)

print('Random 5x5 array')
print (X)
print ('Normalized X')
print (Y)

