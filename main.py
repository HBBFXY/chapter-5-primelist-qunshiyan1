def Primelist(N):
    primes = []
    if N <= 2:
        return ""
    for num in range(2, N):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))  
    return "".join(primes)
print(Primelist(10))  
print(Primelist(2))   
print(Primelist(3))   
    
