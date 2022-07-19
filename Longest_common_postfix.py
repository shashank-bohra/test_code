# Developer     : Shashank 
# Date          : 2022-07-19
# Object        : to find longest common postfix

def long_comm_post(a):
    
    a.sort(key=len) # to get element sorted on length
    
    print('After sort::', a)
    
    #number of elements in array
    x = len(a)
    print('array len is ',x)
    
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
    print("Min length is ", min_len)
    
    # mimimum length is made negative to ristrict the loop that will run from last index of elements
    xx = min_len*-1
    
    #e is used to traverse element in array
    e = 1
    #c is used to traverse the index in the element in array
    c = -1
    
    #flag to checl if loop ran atleast once
    cf = 0  #this will be used to find the postfix string
    flg = 0 #this is used to find that the loop ran atleast once
    # looping to check if characters in first element are matching with character with other elements of array 
    while(c >= xx ):
        while(e < x and a[0][c] == a[e][c]):
            print("e =", e, " c =",c)
            print("a[0][c] is ", a[0][c])
            print("a[e][c] is ", a[e][c])
            e = e+1
            cf = c
            flg = flg+1
            print("1 new e =", e, "1 new c =",c)
        c= c-1
        e = 1 
        
        print("2 new e =", e, "2 new c =",c, 'flag is:', flg)
    result= ""
    if flg > 0:
        result = a[0][cf:]
    if len(result) == 0:
        return"No common postfix"
    return result
    

#ip = ['racecar', 'redcar','car']
#ip = ["asd","xsd", "we"]
#ip = []
ip = ['car']
print(long_comm_post(ip))
