def naturalnum (n):
    i = 0 
    q = 0


    while i * i <= n:
        q = i*i
        i+=1
    
    print("This is the largest square number", q) 
    print("This is the natural number given", n )

naturalnum(89)
