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
