# Developer     : Shashank 
# Date          : 2022-07-19
# Object        : to find longest common prefix

def long_comm_pre(a):
    
    #sorting the array
    a.sort()
    print("After sorting", a)
    
    #number of elements in array
    x = len(a)
    print('Array len is ',x)
    
    # if the array is empty then no element to process
    if(x == 0):
        return "No Element to process"
    
    # if the array has only one element then return the same
    if(x == 1):
        return(a[0])
    
    #finding minimum length of the element in array
    
    min_len = len(a[0])
    
    for ml in range(1,x):
        if(len(a[ml]) < min_len):
            min_len = len(a[ml])
    
    # mimimum length is used to ristrict the loop to find commom prefix
    print("Min length is ", min_len) 
    
    #e is used to traverse element in array
    e = 0
    #c is used to traverse the index in the element in array
    c = 0
    
    # looping to check if characters in first element are matching with character with other elements of array 
    while(e < x and c<min_len and a[0][c] == a[e+1][c]):
        print("e =", e, " c =",c)
        print("a[0][c] is ", a[0][c])
        print("a[e+1][c] is ", a[e+1][c])
        
        e= e+1
        c = c+1 
    result = a[0][0:c]
    if len(result) == 0:
        return"No Common Prefix"
    return result
    

ip = ["kuk","kuko", "kukini","kukazu","kuksu", "kuksui"]
#ip = ["asd","xsd", "we"]
#ip = []
print("Common Prefix is ", long_comm_pre(ip))
