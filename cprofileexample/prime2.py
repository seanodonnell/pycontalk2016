# http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python

def primes_sieve1(limit):
    limitn = limit+1
    # switch the list for a dict
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

print primes_sieve1(2000000)
