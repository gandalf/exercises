"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import itertools
import math


def is_prime_number(n):
    divisor = 3
    is_prime = False

    if n == 2 or n == 3:
        return True

    if n % 2 != 0:
        while True:
            if n % divisor == 0:
                is_prime = False
                break
            elif divisor * divisor > n:
                is_prime = True
                break

            divisor += 2

    return is_prime

l_prime = 0
limit = 600851475143

numbers = lambda stop: iter(itertools.count().next, stop)
r = numbers(math.floor(math.sqrt(limit)))
r.next()

print(math.floor(math.sqrt(limit)))

while True:
    try:
        number = r.next()

        if limit % number == 0:
            if is_prime_number(number):
                l_prime = number
    except StopIteration:
        break

print(l_prime)