f = open("task1_input.txt", "r")
fp = open("task1_output.txt", "w")

def sortSecond(val):    #A function to allow manual sorting.
    return val[1] 

def maxAssignment(arr, n):   
    arr.sort(key=sortSecond)    #sorting by 2nd element
    selected = []       #queue 
    selected.append(arr[0])      
    count = 1
    f = arr[0][1]       #finishing time of first assignment

    for i in range(1,len(arr)):
        s = arr[i][0]
        if(s >= f):
            count += 1
            f = arr[i][1]
            selected.append(arr[i])
            
    fp.write(str(count))
    fp.write("\n")
    for j,k in selected:
        assign = str(j) + " " + str(k)
        fp.write(assign) 
        fp.write("\n")        
    
#input1
n1 = int(f.readline())
list1 = [] 
for i in range(n1):
    input1 = f.readline()
    s, e = list(map(int, input1.split())) #starting and ending times
    list1.append([s,e])  
maxAssignment(list1, n1)
#input2
n2 = int(f.readline())
list2 = [] 
for i in range(n2):
    input2 = f.readline()
    s, e = list(map(int, input2.split())) #starting and ending times
    list2.append([s,e])  
maxAssignment(list2, n2)

f.close() 
fp.close() 