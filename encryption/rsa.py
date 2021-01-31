from math import *
from random import *

# RSA algo
# 1. generate 2 prime (p & q) such that p!=q
# 2. Calculate n = p*q
# 3. calculate phi(n) = (p-1)*(q-1)
# 4. choose e such than gcd(e,phi(n))=1 and 1<e<phi(n) Requires Mobius function
# 5. Calculate d = e^(-1) % phi(n)
# 6. Public key - {e,n} and private key - {d,n}



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
    random_range_start = randint(1000,10000)
    random_range_end = randint(random_range_start,100000)
    primes = []
    
    for i in range(random_range_start,random_range_end):
        if(is_prime(i)):
            length = length - 1
            primes.append(i)
        else:
            continue
        if(length<=0):
            return choice(primes)
            


def Multiply(p,q):
    return p*q

def phi(p,q):
    return Multiply(p-1,q-1)


def choose_e(number):
    for i in range(2,number,1):
        if( is_prime(i)==True and gcd(i,number)==1):
            return i

def choose_d(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        # a = e (exponent) and m -> phi_n
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x
    


def main():
    p = -1
    q = -1
    while(p==q):
        p = PrimeGenerator()
        q = PrimeGenerator()
    
    n = Multiply(p,q)
    phi_n = phi(p,q)
    e=choose_e(phi_n)
    seed()
    # k = randint(2,10)
    k = 2
    d = choose_d(e,phi_n)
    # d = (1 + (k*phi_n))/e
    # d = int(d)
    print("p : ",p,"q : ",q,"n : ",n,'phin_n',phi_n,"e:",e,"d : ",d)
    return e,n,d,n

def GenerateKeys():
    e,n,d,n = main()
    # Public keys & Private keys 
    keys = {'public_keys':[e,n],"private_keys":[d,n]}
    return keys

print(GenerateKeys())


