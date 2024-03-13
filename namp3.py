# minimum dimensions
import numpy as np
a = np.array([1, 2, 3, 4, 5], ndmin = 6)
print(a)



#dtype parameter
import numpy as np
a = np.array([1, 2, 3], dtype = int)
print(a)



import numpy as np
a = np.arange(0, 60,5)
a = a.reshape(4, 3)
print("ordinary array is:")
print(a)
print('\n')
print('modified array is:')
for x in np.nditer(a):
    print(x)
    
    
    
    
    
    
    import numpy as np
    a = np.arange(0, 60, 5)
    a = a.reshape(4, 5)
    print('ordinary array is:')
    print(a)
    print('\n')
    print('transpose of the original array is:')
    b = a.T
    print(b)
    print('\n')
    print('modified array is:')
    for x in np.nditer(b):
        print(x)
    