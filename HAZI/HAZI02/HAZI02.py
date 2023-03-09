import numpy as np
## first task 
def column_swap(input_array):
    input_array=np.array(input_array)      
    return input_array[:,[1,0]]
##second task
def compare_two_array(array1,array2) -> np.array:
    output=[]
    for i in range(0,len(array1)):
        for j in range(0,len(array2)):
            if array1[i]==array2[j]:
                output.append(i)
    return output
##third task
def get_array_shape(input_array) -> np.array:
    input_array=np.array(input_array)
    output = {}
    output["sor"]=np.shape(input_array)[0]
    output["oszlop"]=np.shape(input_array)[1]
    output["melyseg"]=np.shape(input_array)[0]-1   
    return output
##fourth task
def encode_Y(input_array,n):
    input_array=np.array(input_array)
    output=[]
    for i in range(n):
        output.append(list())
        for j in range(n):
            if input_array[i]==j:
                output[i].append(1)
            else:
                output[i].append(0)
    return output
##fifth task
def decode_Y(input_array,n) -> np.array:
    input_array=np.array(input_array)
    output=[]
    for i in range(0,len(input_array)):
        for j in range(n):
            if input_array[i][j]==1:
                output.append(j)            
    return output
##sixth task
def eval_classification(input_array):   
     maxv=max(input_array[1])
     maxi = list(input_array[1]).index(maxv)
     return input_array[0][maxi]
##seventh task
def replace_odd_numbers(input_array):
     input_array=np.array(input_array)
     idxs=np.where(input_array%2!=0)
     for idx in range(0,len(idxs)):
         input_array[idxs]=-1
     return input_array
##eighth task
def replace_by_value(input_array,n):
    input_array=np.array(input_array)
    idxs = np.where(input_array<n)
    idxs2= np.where(input_array>=n)
    idxs.__add__(idxs2)
    for idxs in idxs:
        input_array[idxs] = -1
        input_array[idxs2] = 1
    return input_array
##ninth task
def array_multi(input_array):   
    return np.prod(input_array)
##tenth task
def array_multi_2d(array1,array2):
    return [np.prod(array1),np.prod(array2)]