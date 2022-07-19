# Developer     : Shashank 
# Date          : 2022-07-19
# Object        : to find longest common postfix

def long_comm_post(a):
    
    a.sort(key=len) # to get element sorted on length
    
    print('after sort::', a)
    
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
    
    #making the minimum length minus to traverse the elements from last index
    xx = min_len*-1
    
    #e is used to traverse element in array
    e = 1
    #c is used to traverse the index in the element in array
    c = -1
    
    #flag to checl if loop ran atleast once
    flg = 0
    
    # looping to check if characters in first element are matching with character with other elements of array 
    while(e < x ):
        while(c>= xx and a[0][c] == a[e][c]):
            print("e =", e, " c =",c)
            print("a[0][c] is ", a[0][c])
            print("a[e][c] is ", a[e][c])
            c = c-1
            flg = flg+1
            print("1 new e =", e, "1 new c =",c)
        e= e+1
        c= -1
        
        print("2 new e =", e, "2 new c =",c, 'flag is:', flg)
    result= ""
    if flg > 0:
        result = a[0][c:]
    if len(result) == 0:
        return"No common postfix"
    return result
    

ip = ['racecar', 'redcar','car', 'bar', 'sr']
#ip = ["asd","xsd", "we"]
#ip = []
print("common postfix is ", long_comm_post(ip))
