# Developer     : Shashank 
# Date          : 2022-07-19
# Object        : to find longest common prefix

def long_comm_pre(a):
    
    #sorting the array
    a.sort()
    print("after sorting", a)
    
    #number of elements in array
    x = len(a)
    print('array len is ',x)
    
    if(x == 0):
        return "No Element to process"
    
    min_len = len(a[0])
    for ml in range(1,x):
        if(len(a[ml]) < min_len):
            min_len = len(a[ml])
    
    print("min_len is ", min_len)
    
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
        return"No common prefix"
    return result
    

ip = ["kuk","kuko", "kukini","kukazu","kuksu", "kuksui"]
#ip = ["asd","xsd", "we"]
#ip = []
print("common prefix is ", long_comm_pre(ip))
