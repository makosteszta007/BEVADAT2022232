##first task
def subset(input_list,start_index,end_index):
    return input_list[start_index:end_index]
##second task
def every_nth(input_list,n):
    output=[]
    for idx in range(0,len(input_list),n):
        output.append(input_list[idx])
    return output
##third task
def unique(input_list):
    a = 0
    list(input_list).sort()
    for idx in range(0,len(input_list)-1):
        if input_list[idx]<input_list[idx+1]:
            a+=1
    if a==len(input_list)-1:
        return True
    else:
        return False
##fourth task
def flatten(input_list):
    a = len(input_list)
    for idx in range(0,a):
         for idx2 in range(0,len(input_list[0])):
             input_list.append(input_list[0][idx2])
         input_list.remove(input_list[0])
    return input_list
##fifth task
def merge_lists(*args):
    output=[]
    for arg in args:      
        for idx in range(0,len(arg)):
            output.append(arg[idx])
    return output
##sixth task
def reverse_tuples(input_list):      
    for idx in range(0,len(input_list)):       
         input_list[idx] = (tuple(reversed(input_list[idx])))
    return input_list
##seventh task
def remove_duplicates(input_list):
    input_list = list(dict.fromkeys(input_list))
    return input_list
##eighth task
def transpose(input_matrix):
    a=len(input_matrix)
    for i in range(a):
        for j in range(i+1,a):
            input_matrix[i][j], input_matrix[j][i] = input_matrix[j][i], input_matrix[i][j]
    return input_matrix
##ninth task
def split_into_chunks(input_list,chunk_size):      
    a = len(input_list)
    for idx in range(0,int(a/chunk_size)):
        input_list.append(list())
        for idx2 in range(0,chunk_size):            
             input_list[len(input_list)-1].append(input_list[0])
             input_list.remove(input_list[0])
    if len(input_list)>chunk_size:
         input_list.append(list())
         for i in range(0,a%chunk_size):
             input_list[len(input_list)-1].append(input_list[0])
             input_list.remove(input_list[0])
    return input_list
##tenth task
def merge_dicts(*dicts):
    output={}    
    for dict in dicts:            
        output.update(dict)
    return output
##eleventh task
def by_parity(input_list):
    output={}  
    even_list=list()
    odd_list=list()
    for idx in range(0,len(input_list)):
        if input_list[idx]%2==0:
           even_list.append(input_list[idx])           
        else:
           odd_list.append(input_list[idx])
    output['even'] = even_list
    output['odd'] = odd_list
    return output
##twelfth task
def mean_key_value(input_dict):
    for idx in input_dict.keys():
        a=0
        for i in input_dict[idx]:
            a+=i
        input_dict[idx]=a/len(input_dict[idx])
    return input_dict
