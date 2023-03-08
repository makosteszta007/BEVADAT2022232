import numpy as np
## first task 
def column_swap(input_array):
    input_array=np.array(input_array)      
    return input_array[:,[1,0]]
print(column_swap([[1,2],[3,4]]))
