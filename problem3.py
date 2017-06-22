import math

def isPrime(n):
    isPrime = True
    for i in range(1, n):
        if i!=1 and n % i == 0 :
            isPrime = False
    return isPrime

print(isPrime(10))

def primeFactors(n):
    primeFactors = []
    for i in range(1, int(math.sqrt(n))):
        if isPrime(i) and n % i == 0:
            primeFactors.append(i)
            print (primeFactors)
    return primeFactors

print(primeFactors(600851475143))






