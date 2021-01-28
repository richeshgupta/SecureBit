from math import *
from random import *

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

def PrimeGenerator(length=23):
    """ Generates prime number between randomised start and end points 
     args: length of primes you want to juggle with
     returns: 1 prime number
     """
    seed()
    random_range_start = randint(1000,10000000)
    random_range_end = randint(random_range_start,100000000)
    primes = []
    
    for i in range(random_range_start,random_range_end):
        if(is_prime(i)):
            length = length - 1
            primes.append(i)
        else:
            continue
        if(length<=0):
            return choice(primes)
            
print(PrimeGenerator())


