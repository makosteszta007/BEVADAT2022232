import numpy as np
## first task 
def column_swap(input_array):
        return np.fliplr(input_array)
##second task
def compare_two_array(array1,array2):  
   return np.where(np.array(array1)==np.array(array2))[0]
print(compare_two_array([1,2,3],[3,2,1]))
##third task
def get_array_shape(input_array): 
    input_array=np.matrix(input_array)
    rows,columns = np.array(input_array).shape
    return f"sor: {rows} oszlop: {columns} melyseg: {rows-1}"
##fourth task
def encode_Y(input_array,n):    
    return np.eye(n)[np.array(input_array).reshape(-1)]
##fifth task
def decode_Y(input_array) -> np.array:  
    return np.where(np.array(input_array)==1)[1]
##sixth task
def eval_classification(input_array):
     return input_array[0][list(input_array[1]).index(max(input_array[1]))]
##seventh task
def replace_odd_numbers(input_array):    
     return np.where(np.array(input_array)%2==0,input_array,-1)
##eighth task
def replace_by_value(input_array,n):
    input_array= np.where(np.array(input_array)>=n,input_array,-1) 
    return np.where(np.array(input_array)<n,input_array,1)
##ninth task
def array_multi(input_array):   
    return np.prod(input_array)
##tenth task
def array_multi_2d(array1,array2):
    return [np.prod(array1),np.prod(array2)]
##eleventh task
def add_border(input_array)->np.array:
    return np.pad(input_array, pad_width=1, mode='constant', constant_values=0)
##twelfth task
def list_days(date1,date2): 
    return np.arange(np.datetime64(date1),np.datetime64(date2),np.timedelta64(1, "D"))
##thirteenth task
def current_date():
    return np.datetime64('today')
##fourteenth task
def sec_from_1970():
    return int((np.datetime64('today')-np.datetime64('1970-01-01'))/np.timedelta64(1, "s"))