##first task
def contains_odd(input_list):
    odd = False
    for idx in range(0,len(input_list)):
        if input_list[idx]%2!=0:
            odd = True
    return odd
##second task
def is_odd(input_list):
     for idx in range(0,len(input_list)):
        if input_list[idx]%2!=0:
            input_list[idx]=True
        else:
            input_list[idx]=False
     return input_list
 ##third task
def element_wise_sum(input_list_1,input_list_2):
    output=[0,0]   
    for idx in range(0,max(len(input_list_1),len(input_list_2))):
        if idx < len(input_list_1):
            output[0] += input_list_1[idx]
        if idx < len(input_list_2):
            output[1] += input_list_2[idx]
    return output
##fourth task
def dict_to_list(input_dict):
    output=list()
    for key,value in input_dict.items():
        output.append((key,value))
    return output

