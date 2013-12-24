"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(num):
    text = str(num)
    reversed_text = text[::-1]

    if text == reversed_text:
        return True
    else:
        return False

l_palindrome = 0
numbers = range(100, 1000)

for n in range(100, 1000):
    for number in numbers:
        p = n * number

        if is_palindrome(p) and p > l_palindrome:
            l_palindrome = p

print l_palindrome
