## first task
def subset(start_index,end_index):
    output=[]
    for idx in range(start_index, end_index):
        output.append(input_list[idx])
    return output
##second task
def every_nth(input_list):
    output=[]
    for idx in range(0,len(input_list),3):
        output.append(input_list[idx])
    return output
##third task
def unique(input_list):   
    output = int()
    for idx in range(0,len(input_list)):
       if input_list[idx]==4:
        output = input_list[idx]
    return output==4
##fourth task
def flatten(input_list):
    output=[]
    for idx in range(0,len(input_list)):
         output.append([input_list[idx]])
    return output
##fifth task
def merge_list(*args):
    output=[]
    for arg in range(1):      
          output.append(args)
    return output
##sixth task
def reverse_tuples(input_list):  
    output=[]
    for idx in range(0,len(input_list)):       
        output.append(tuple(reversed(input_list[idx])))
    return output
##seventh task
