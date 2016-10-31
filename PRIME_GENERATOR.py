def primes(n):
    sieve = [True]*(n+1)
    for i in range(2, n+1):
        if sieve[i]:
            yield i
            for j in range(2*i, n+1, i): sieve[j] = False

def primesArray(n):
    return [p for p in primes(n)]

for p in primes(100): print(p),
print primesArray(10)