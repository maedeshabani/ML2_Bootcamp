
def local_max(input_array:list):
    tempcount=0
    for i in range(len(input_array)-1):
        if i==0:
            input_array[0]
        elif i==-1:
            input_array[-1]
        else:
            if input_array[i]> input_array[i+1] :
                input_array[i+1]=input_array[i]
                tempcount +=1
            
            elif input_array[i]> input_array[i-1] :
                input_array[i-1]=input_array[i]
                tempcount +=1

    return(tempcount,input_array)



def reducer_func(input:int):
    split_num=[digit for digit in str(input)]
    for i in range(len(split_num)-1):
        x= str(int(split_num[i]) + int(split_num[i+1]))
        reduced_number = list(split_num[:i] + [x] + split_num[i+2:])
    return int(''.join(reduced_number))


def is_unstable(input_str:str):
    for i in range(len(input_str)-1):
        if input_str[i] != input_str[i+1] and input_str[i] != input_str[i-1] :
            return True
    else:
        return False

def is_well_modify(input:str):
    if input.replace('?','0'):
        is_unstable(input)
    elif input.replace('?','1'):
        is_unstable(input)
    else:
        return False
