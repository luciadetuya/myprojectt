def SumMaxMinAvgCount(): 
    n = 0 
    s = 0 
    m = float('inf')
    x = int(input("Enter a natural number: "))
    while x != -1: 
        n = n+1 
        s = s+x 
        m = min(m,x)
        x = int(input("Enter -1 to terminate code or a natural number: "))
    if n == 0: 
        print ("Input is not given")
        
    else: 
        a = s/n
        print ("This is the count = ", n) 
        print ("This is the sum = " , s )
        print ("This is the minimun = ", m)
        print ("This is the mean = ", a)
        
SumMaxMinAvgCount()

## it looks like I learned how to use git today'
