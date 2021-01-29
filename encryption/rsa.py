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

def Multiply(p,q):
    return p*q

def phi(p,q):
    return Multiply(p-1,q-1)


def choose_gcd(number):
    for i in range(2,number,1):
        if( is_prime(i)==True and gcd(i,number)==1):
            return i
        
def main():
    p = -1
    q = -1
    while(p==q):
        p = PrimeGenerator()
        q = PrimeGenerator()
    
    n = Multiply(p,q)
    phi_n = phi(p,q)
    e=choose_gcd(phi_n)
    d = pow(e,-1)%phi_n
    print("p : ",p,"q : ",q,"n : ",n,'phin_n',phi_n,"e:",e,"d : ",d)
    return e,n,d,n

def GenerateKeys():
    e,n,d,n = main()
    # Public keys & Private keys 
    keys = {'public_keys':[e,n],"private_keys":[d,n]}
    return keys

print(GenerateKeys())


