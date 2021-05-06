from math import *
from random import *

# RSA algo
# 1. generate 2 prime (p & q) such that p!=q
# 2. Calculate n = p*q
# 3. calculate phi(n) = (p-1)*(q-1)
# 4. choose e such than gcd(e,phi(n))=1 and 1<e<phi(n) Requires Mobius function
# 5. Calculate d = e^(-1) % phi(n)
# 6. Public key - {e,n} and private key - {d,n}

alpha_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,' ':27}
key_list = list(alpha_dict.keys())

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

def PrimeGenerator(length=2):
    """ Generates prime number between randomised start and end points 
     args: length of primes you want to juggle with
     returns: 1 prime number
     """
    seed()
    random_range_start = randint(100,1000)
    random_range_end = randint(random_range_start,10000)
    primes = []
    
    for i in range(random_range_start,random_range_end):
        if(is_prime(i)):
            length = length - 1
            primes.append(i)
        else:
            continue
        if(length<=0):
            return choice(primes)
        # return choice(primes)
            


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
    
def main(string):
    p = -1
    q = -1
    while(p==q):
        p = PrimeGenerator()
        q = PrimeGenerator()
    
    n = Multiply(p,q)
    phi_n = phi(p,q)
    e=choose_e(phi_n)
    seed()
    d = choose_d(e,phi_n)
    
    
    print('')
    numeric_list = []
    cipher_number = []
    txt = []
    print("String : ",string)
    for i in string:
        numeric_list = numeric_list + [alpha_dict[i],]
        
    for i in numeric_list:
        cipher_number = cipher_number + [encryption(i,d,e,n),]
        
    # print('Cipher List= ',cipher_number)
    print('Encrypted Number= ',end=' ')

    for i in cipher_number:
        print(i, end='')

    print('\n')

    # for i in cipher_number:
    #     txt = txt + [decryption(i,d,n),]

    # print('Decrypted List= ',txt)

    # print('Decrypted Number= ',end='')

    # for i in txt:
    #     print(i, end='')
    print('\n')
    # print('Decrypted String= ',end='')
    
    # for i in numeric_list:
    #     print(key_list[i-1],end='')
    # print('\n')
    
    return e,n,d,n,cipher_number

def GenerateKeys(txt):
    e,n,d,n,cipher = main(txt)
    # Public keys & Private keys 
    keys = {'public_keys':[e,n],"private_keys":[d,n]}
    print(keys)
    return keys,cipher


def encryption(txt,d,e,n):
    cipher_txt = (e*txt)%n
    return cipher_txt

def decryption(cipher_txt,d,n):
    txt = (cipher_txt*d)%n
    return txt

def ExternalEncrypt(txt):
    e,n,d,n,cipher = main(txt)
    cipher_text=""
    print("Cipher_array")
    for i in cipher:
        cipher_text+=str(i)+","
    return cipher_text


# print(ExternalEncrypt("hello"))