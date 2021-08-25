f = open("task2_input.txt", "r")
fp = open("task2_output.txt", "w")

def sortSecond(val):    #A function to allow manual sorting.
    return val[1] 

def maxAssignment(arr, m):   
    arr.sort(key=sortSecond)    #sorting by 2nd element
    selected = []       #queue       
    count = 0
    
    dict = {}
    for k in range(m):
        dict[k] = 0
    
    for i in range(0,len(arr)):
        for j in range(2):  
            if(arr[i] in selected):
                continue
            
            f = dict[j] 
            s = arr[i][0] 
            if(s >= f):
                count += 1 
                dict[j] = arr[i][1] 
                selected.append(arr[i]) 

    fp.write(str(count)) 
    fp.write("\n")

#input1
nm1 = f.readline()
n1, m1 = list(map(int, nm1.split())) 
list1 = [] 
for i in range(n1):
    input1 = f.readline()
    s, e = list(map(int, input1.split())) #starting and ending times
    list1.append([s,e])   
maxAssignment(list1, m1) 

#input2
nm2 = f.readline()
n2,m2 = list(map(int, nm2.split()))
list2 = []
for i in range(n2): 
    input2 = f.readline()
    s, e = list(map(int, input2.split())) #starting and ending times
    list2.append([s,e])  
maxAssignment(list2, m2)  

f.close() 
fp.close() 