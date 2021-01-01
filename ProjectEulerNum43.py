# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.
import itertools
import time # This program takes about 45 seconds to run on my Lenovo Thinkpad -- Matthew Bruno 12/31/2020

start = time.time()

digits = [0,1,2,3,4,5,6,7,8,9]
primes = []
pandigitals = []
special_pandigitals = []
answer = 0

def sieve_eratosthenes(n):
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primes

sieve_eratosthenes(19)

def deconstruct(num): #turns number into a list of its digits
    digits = [int(k) for k in str(num)]
    return digits

def convert(list): #turns digit list into a number
    num = sum(digit * pow(10,i) for i, digit in enumerate(list[::-1]))
    return (num)

def property_check(num):
    digits = deconstruct(num)
    check = []
    for k in range(2,9):
        three_digits = []
        three_digits.append(digits[k-1])
        three_digits.append(digits[k])
        three_digits.append(digits[k+1])
        if convert(three_digits) % primes[k-2] == 0:
            check.append(True)
        else:
            check.append(False)
            break
    if all(check):
        return True
    else:
        return False

perms_list = set(itertools.permutations(digits))

for perm in perms_list:
    if len(str(convert(perm))) == 10:
        pandigitals.append(convert(perm))

for k in pandigitals:
    if property_check(k):
        special_pandigitals.append(k)
    else:
        continue

for i in special_pandigitals:
    answer += i

print(answer)

stop = time.time()
print("Time: ", stop - start)