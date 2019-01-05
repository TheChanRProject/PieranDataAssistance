# import numpy as np
#
# def count_primes(n):
#     from math import sqrt
#     primes = np.arange(3, n + 1, 2)
#     isprime = np.ones((n - 1) // 2, dtype=bool)
#     for factor in primes[:int(sqrt(n))]:
#         if isprime[(factor - 2) // 2]:
#             isprime[(factor * 3 - 2) // 2:(n - 1) // 2:factor] = 0
#     return len(np.insert(primes[isprime], 0, 2))
#
# count_primes(100)

def is_prime(num):
    for n in range(2,num):
        return not num%n == 0
    else:
        return True

primes = []
number = int(input("Put in a number:"))
for num in range(2,number):
    if is_prime(num):
        primes.append(num)
    else:
        pass
print(f"The following numbers are prime: {primes}")
