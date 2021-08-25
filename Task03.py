f = open("task3_input.txt", "r")
fp = open("task3_output.txt", "w") 

def choreSelection(arr, order):   
    arr.sort()    #sorting in ascending order
    
    stack = []       #queue       
    ind, jack, jill  = 0, 0, 0
    seq = []
    
    for c in order: 
        if(c == "J"):
            stack.append(arr[ind]) 
            seq.append(arr[ind])
            jack += arr[ind]
            ind += 1
        
        elif(c == "j"):
            value = stack.pop() 
            seq.append(value)
            jill += value
            
    for i in seq:
        fp.write(str(i))
    fp.write("\n")
    a = "{} will work for {} hours".format("Jack", jack)
    b = "{} will work for {} hours".format("Jill", jill)
    fp.write(a)
    fp.write("\n")
    fp.write(b)
    fp.write("\n")

#input1
n1 = int(f.readline())
tasks1 = f.readline() 
calls1 = f.readline()
list1 = list(map(int, tasks1.split()))
choreSelection(list1, calls1)

#input2
n2 = int(f.readline())
tasks2 = f.readline() 
calls2 = f.readline()
list2 = list(map(int, tasks2.split()))
choreSelection(list2, calls2)

f.close() 
fp.close() 