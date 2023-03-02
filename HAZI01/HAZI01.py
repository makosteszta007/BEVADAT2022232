## first task
input_list = [0,1,2,3,4,5,6,7,8,9]
def subset(start_index,end_index):
    output=[]
    for idx in range(start_index, end_index):
        output.append(input_list[idx])
    return output
##second task
def every_nth(n):
    output=[]
    for idx in range(0,11,n):
        output.append(input_list[idx])
    return output

