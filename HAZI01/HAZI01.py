## first task
input_list = [0,1,2,3,4,5,6,7,8,9]
def subset(start_index,end_index):
    output=[]
    for idx in range(start_index, end_index):
        output.append(input_list[idx])
    return output
##second task
def every_nth(input_list):
    output=[]
    for idx in range(0,10,3):
        output.append(input_list[idx])
    return output
##third task
def unique(input_list):   
    output = int()
    for idx in range(0,10):
       if input_list[idx]==4:
        output = input_list[idx]
    return output==4
##fourth task
def flatten(input_list):
    output=[]
    for idx in range(0,10):
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
    for idx in range(0,10):     
      output.append(input_list[9-idx])     
    return output
