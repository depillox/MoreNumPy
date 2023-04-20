import numpy as np
from functionsPackage.functions import *

def demo():
    '''
    Demonstrate all the functions we'll write
    '''
    print(get_odd_values(np.array([1,2,3,4,5,6])))
    print(find_common_values(np.array([1,2,3]), np.array([2,4,6])))
    
    
    answer = F_to_C(42) #This is not a correct type to pass to the function
    print(answer)
    some_data = np.arange(5) #5 element array 
    some_data[0] = 100
    some_data[1] = 0
    some_data[2] = 32
    some_data[3] = 212
    some_data[4] = -40
    answer = F_to_C(some_data) #The value returned by F_to_C is stored in answer 
    print(answer)
    
    