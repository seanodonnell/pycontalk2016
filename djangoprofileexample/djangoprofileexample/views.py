from django.http import HttpResponse

primelist = []

def prime(request):
    global primelist
    limit = 2000
    limitn = limit + 1
    primes = range(2, limitn)

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    primelist += primes
    return HttpResponse(repr(primes))
