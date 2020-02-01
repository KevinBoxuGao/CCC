T = int(input())
inputs = []
primes = []

for i in range(T):
    inputs.append(2*int(input()))

n = max(inputs)
isPrime = (n+1)*[True]

isPrime[0] = isPrime[1] = False

for i in range(2, n+1):
    if isPrime[i] and i*i <= n:
        j = i*i
        while j <= n:
            isPrime[j] = False
            j += i

for i, prime in enumerate(isPrime):
    if prime:
        primes.append(i)

for N in inputs:
    for prime in primes:
        secondValue = N-prime
        if isPrime[secondValue]:
            print(str(prime) + " " + str(secondValue))
            break
