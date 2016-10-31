# from http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python

def primes_sieve(limit):
    limitn = limit+1
    primes = range(2, limitn)

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

print primes_sieve(20000)



