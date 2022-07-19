# my code prefix
# to find longest common prefix

def long_comm_pre(a):
    a.sort()
    print("after sorting", a)
    
    #element in array
    x = len(a)
    print('array len is ',x)
    
    if(x == 0):
        return "No Element to process"
    
    min_len = len(a[0])
    for ml in range(1,x):
        if(len(a[ml]) < min_len):
            min_len = len(a[ml])
    
    print("min_len is ", min_len)
    
    #e is for element
    e = 0
    #c is for character
    c = 0
    
     
    while(e < x and c<min_len and a[0][c] == a[e+1][c]):
        print("e =", e, " c =",c)
        print("a[0][c] is ", a[0][c])
        print("a[e+1][c] is ", a[e+1][c])
        
        e= e+1
        c = c+1 
    ans = a[0][0:c]
    if len(ans) == 0:
        return"No common prefix"
    return ans
    

ip = ["kuk","kuko", "kukini","kukazu","kuksu", "kuksui"]
#ip = ["asd","xsd", "we"]
#ip = []
print("common prefix is ", long_comm_pre(ip))
