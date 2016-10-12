primes = []
for n in range(2, 101):
    for divisor in range(2, n):
        if n % divisor == 0: 
        	break
    else: 
    	primes.append(n)
print(primes)