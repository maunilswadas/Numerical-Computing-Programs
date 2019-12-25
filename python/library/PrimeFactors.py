def primeSieve(n):
    sieve = [True for i in range(n + 1)] 
    p = 2
    while p * p <= n:
        if sieve[p] == True:
            for i in range(p * 2, n + 1, p): 
                sieve[i] = False
        p += 1
    sieve[0]= False
    sieve[1]= False
    
    
    return sieve