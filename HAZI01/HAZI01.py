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
    for idx in range(0,len(input_list)):
       if input_list[idx]==4:
        return True
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
def merge_list(*args):
    output=[]
    for arg in range(1):      
          output.append(args)
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
def transpose(input_list):
    a = len(input_list)
    for idx in range(0,a):
         for idx2 in range(0,len(input_list[0])):
             input_list.append(input_list[0][idx2])
         input_list.remove(input_list[0])
    return input_list
##ninth task
def split_into_chunks(input_list,chunk_size):      
    a = len(input_list)
    for idx in range(0,a):
         for idx2 in range(0,len(input_list[0])):
             input_list.append(input_list[0][idx2])
         input_list.remove(input_list[0])
    result = []
    chunk = []
    for item in input_list:
        chunk.append(item)
        if len(chunk) == chunk_size:
            result.append(chunk)
            chunk = []       
    return result
    