from math import sqrt
from math import floor


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]

    p = 2
    while p*p <= n:

        if prime[p]:

            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    return [i for i in range(2, n+1) if prime[i]]


def segemeted_sieve_of_eratosthenes(n):
    limit = floor(sqrt(n))+1
    primes = sieve_of_eratosthenes(limit)
    low = limit
    high = 2*limit
    res = [p for p in primes]
    while low < n:

        if high > n:
            high = n

        mark = [True for i in range(limit+1)]

        for p in primes:

            il = floor(low/p)*p
            if il < low:
                il += p

            for i in range(il, high, p):
                mark[i-low] = False

        for i in range(low, high):
            if mark[i-low]:
                res.append(i)

        low += limit
        high += limit
    return res


def main():
    print(sieve_of_eratosthenes(10))
    print(sieve_of_eratosthenes(20))
    print(sieve_of_eratosthenes(50))

    print('*'*20)

    print(segemeted_sieve_of_eratosthenes(10))
    print(segemeted_sieve_of_eratosthenes(20))
    print(segemeted_sieve_of_eratosthenes(50))


if __name__ == "__main__":
    main()
