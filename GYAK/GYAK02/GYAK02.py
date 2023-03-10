import numpy as np
##first task
def create_array(size=(2,2))->np.array:
    return np.zeros(size)
##second task
def set_one(input_array)->np.array:  
    input_array=np.array(input_array)
    np.fill_diagonal(input_array,1)   
    return input_array
##third task
def do_transpose(input_matrix)->np.array:
    input_matrix=np.transpose(input_matrix)
    return input_matrix
##fourth task
def round_array(input_array,n=2)->np.array:        
    return np.array(input_array).round(n)
##fifth task
def bool_array(input_array)->np.array:
    return np.array(input_array,dtype=bool)
##sixth task
def invert_bool_array(input_array)->np.array:
    return np.invert(np.array(input_array,dtype=bool))
##seventh task
def flatten(input_array)->np.array:    
    return np.ndarray.flatten(np.array(input_array))
