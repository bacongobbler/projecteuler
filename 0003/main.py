def prime_factors(n):
    return [ d for d in range(2,n/2) if is_prime(d) and n % d == 0 ]

def is_prime(n):
    return all(n % i for i in xrange(2, n/2))

if __name__ == '__main__':
    # WARNING: computer will crash when testing this
    print(prime_factors(600851475143)[-1])
