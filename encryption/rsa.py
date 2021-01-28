from math import *
from random import randint,sample,seed,shuffle

# RSA algo
# 1. generate 2 prime (p & q) such that p!=q


def is_prime(number):
    """ returns if number is prime or not """
    if(number<=1):
        return False
    if(number==2):
        return True
    for i in range(2,int(sqrt(number)+1)):
        if(number%i==0):
            return False

    return True

def PrimeGenerator():
    """ Generates prime number between randomised start and end points """
    seed()
    random_range_start = randint(1000,1000000)
    random_range_end = randint(random_range_start,100000000)
    primes = []
    length = 2
    for i in range(random_range_start,random_range_end):
        if(is_prime(i)):
            length = length - 1
            primes.append(i)
        else:
            continue
        if(length<=0):
            # primes= shuffle(primes)
            return primes
    

    

print(PrimeGenerator())


