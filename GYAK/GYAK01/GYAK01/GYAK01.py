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
