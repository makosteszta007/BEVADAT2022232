import numpy as np
##first task
def create_array(size=(2,2))->np.array:
    return np.zeros(size)
##second task
def set_one(input_array):  
    input_array=np.array(input_array)
    np.fill_diagonal(input_array,1)   
    return input_array
print(set_one([[0,2],[2,3]]))
