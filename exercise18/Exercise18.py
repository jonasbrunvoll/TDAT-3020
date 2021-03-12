#!/usr/bin/env python
# coding: utf-8

# #### Task 1a
# 
# 

# In[3]:


num1 = str(bin(72).replace("0b", ""))
num2 = str(bin(136).replace("0b", ""))
print('72 =', num1,', 136 =',num2)


# #### Task 1a
# 
# 72 / 2 = 36 + 0.    
# 36 / 2 = 34 + 0.  
# 34 / 2 = 17 + 0.   
# 17 / 2 =  8 + 1.   
#  8 / 2 =  4 + 0.    
#  4 / 2 =  2 + 0.    
#  2 / 2 =  1 + 0.   
#  1 / 2 =  0 + 1.    
# 
# 72 = 0100 1000.
# 
# 136 / 2 = 68 + 0.  
# 36 / 2 = 34 + 0.  
# 34 / 2 = 17 + 0.   
# 17 / 2 =  8 + 1.   
#  8 / 2 =  4 + 0.    
#  4 / 2 =  2 + 0.    
#  2 / 2 =  1 + 0.   
#  1 / 2 =  0 + 1. 
# 
# 136 = 1000 1000.
# 
# 
# 
# 
# #### Task 1b
# 
# a = 11<sup>72</sup> (mod 10001)
# b = 11<sup>136</sup> (mod 10001)
# 
# Setter opp en tabell:   
# - 11<sup>2</sup> = 121 => 121 (mod 10001)  
# - 11<sup>4</sup> = (11<sup>2</sup>)<sup>2</sup> => 4640 (mod 10001)
# - 11<sup>8</sup> = (11<sup>4</sup>)<sup>2</sup> => 7448 (mod 10001)
# - 11<sup>16</sup> = (11<sup>8</sup>)<sup>2</sup> => 7125 (mod 10001)
# - 11<sup>32</sup> = (11<sup>16</sup>)<sup>2</sup> => 1841 (mod 10001)
# - 11<sup>64</sup> = (11<sup>32</sup>)<sup>2</sup> => 8943 (mod 10001)
# - 11<sup>128</sup> = (11<sup>64</sup>)<sup>2</sup> => 9253 (mod 10001)
# 
# 
# Finner a:   
# 72 = 64 + 8    
# 11<sup>72</sup> = 11<sup>64</sup>*11<sup>8</sup> = 8943 * 7448 => 804 (mod 10001)  
# 
# a = 804  
# 
# Finner b:  
# 136 = 128 + 8  
# 11<sup>136</sup> = 11<sup>128</sup>*11<sup>8</sup> = 9253 * 7448 => 9454 (mod 10001) 
# 
# b = 9454  
# 
# 
# #### Task 1c   
# gcd( a, 10001) = gcd( 804, 10001) = 1.   
# Utregning:  
# - 10001 = 12 * 804 + 353.
# -  804 = 2 * 353 + 98. 
# -  353 = 3 * 98 + 59.
# -  98 = 59 + 39.
# -  59 = 39 + 20.
# -  39 = 20 + 19. 
# -  20 = 19 + 1. 
# -  19 = 19 * 1 + 0.  
# 
# gcd( b, 10001) = gcd( 9454, 10001) = 1.   
# Utregning:  
# - 10001 = 9454 + 547.  
# - 9454 = 17 * 547 + 155.  
# - 547 = 3 * 155 + 82.  
# - 155 = 82 + 73.  
# - 82 = 73 + 9.  
# - 73 = 8 * 9 + 1.  
# - 9 = 9 * 1 + 0.   
# 
# #### Task 1d 
# Alternativ 1:  
# ab = 9454 * 804 = 7601016.  
# 7601016 => 256 (mod 10001). 
# 
# Alternativ 2:  
# a = 11<sup>72</sup>.
# b = 11<sup>136</sup>.
# ab = 11<sup>72</sup> * 11<sup>136</sup> = 11<sup>208</sup>. 
# 
# 208 = 128 + 64 + 16.   
# 11<sup>208</sup>   
# = 11<sup>128</sup> * 11<sup>64</sup> * 11<sup>8</sup>     
# = 9253 * 8943 * 7158  
# => 256 (mod 10001).  
# 

# #### Task 2

# In[4]:


import math

def modularExponentiation(x,e,mod):
    X = x
    expo = e
    Y = 1
    while expo > 0:
        if expo % 2 == 0:
            X = (X * X) % mod
            expo = expo/2
        else:
            Y = (X * Y) % mod
            expo = expo - 1
    return Y

def gcdExtended(a, b):  
    # Base Case  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)    
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 
         
def rsa_create_keys(p, q, e):
    n = p * q
    myN = (p-1)*(q-1)
    g, x, d = gcdExtended(myN,e)
    while d < 0:
        d += myN
    
    return n, e, d
    
    
def rsa_encrypt(messege, n, e):
    c = modularExponentiation(messege, e, n)
    return c 
    
def rsa_decrypt(c, d, n):
    messege = modularExponentiation(c, d, n)
    return messege


# In[5]:


p = 137 
q = 139 
e = 5

messege = 42
n, e, d= rsa_create_keys(p,q,e)
c = rsa_encrypt(messege,n,e)
m = rsa_decrypt(c,d, n)

print('a) Offentlig nøkkel: ({}, {})'.format(n,e))
print('b) Privat nøkkel: ({})'.format(d))
print('c) Krypterer 42 til {}\n   Dekrypterer {} tilbake til {}'.format(c,c,m)) 


# #### Task 3

# In[6]:


import math
    
def factorizeNum(num):
    factors = []
    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                num //= i
                factors.append(i)
    
    factors.sort()
    for num in factors:
        for i in range(2, num):
            if (num % i) == 0:
                newnum = num // i
                for i in range(len(factors)):
                    if factors[i] == num:
                        factors[i] = newnum
                        factors.append(newnum)
    factors.sort()
    return factors

def factorial(num):
    fact = 1
    for i in range(1,num+1): 
        fact = fact * i 
    return fact
    

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
  
 
def pollardMinusOne(B, mod):
    i = 2
    limit = 50
    H = 0
    factors = []
    while i <= B:
        l = factorial(i)
        num = modularExponentiation(2,l, mod) - 1
        hcf = gcd(mod, num)
        if hcf != 1:
            if hcf != mod:
                if (hcf not in factors): 
                    factors.append(hcf)
                if H < hcf:
                    H = hcf  
        i += 1
    return H, factors
        


def guessBPollardMinusOne(limit, mod):
    highestValue = 0
    bHighestValue = 0
    for B in range(2, limit):
        hcf, factors = pollardMinusOne(B, mod)
        if highestValue < hcf:
            highestValue = hcf
            bHighestValue = B
    return bHighestValue, highestValue, factors


# In[7]:


print(factorial(3))


# a
n = 1829 
B = 5 #24 => 59 
a, listA = pollardMinusOne(B, n)
print('a)\n   Når B = {}, blir høyeste primtallsfaktor: {}\n   Liste med primtallsfaktorer: {}'.format(B,a, listA))


#b
n1 = 18779  
n2 = 42583
limit = 100
B1, b1, listB1 = guessBPollardMinusOne(limit, n1)
B2, b2, listB2 = guessBPollardMinusOne(limit, n2)
fact1 = factorizeNum(listB1[1] - 1)
fact2 = factorizeNum(listB2[0] - 1)

print(listB1)

print('\nb)')
print('   {} er en av primtallsfaktorene til {}.'.format(b1,n1))
print('   Vi faktoriserer {} - 1: {}'.format(listB1[1], fact1)) 
print('   Vi ser at B = {} er gir den høyeste fakultetverdien.'.format(fact1[len(fact1)-1], listB1[0]))
print('.  Vi kan derfor være sikker på at B = {} gir oss primtallsfaktoren {}'.format(fact1[len(fact1)-1], listB1[0]))

print('\n   {} er en av primtallsfaktorene til {}'.format(b2,n2))
print('   Vi faktoriserer {} - 1: {}'.format((listB2[0]), fact2))
print('   Vi ser at B = {}^{} = {} er gir den høyeste fakultetverdien.'.format(2,5,32, listB2[0]))
print('.  Vi kan derfor være sikker på at B = {} gir oss primtallsfaktoren {}'.format(32, listB2[0]))


#c
limit = 100 # B = 100! max
n = 6319
B, c, listC = guessBPollardMinusOne(limit, n)
print('\nc)\n   B = {} gir høyeste primtallsfaktor: {}'.format(B,c))
print('   Liste med primtallsfaktorer: {}, når max B = {}'.format(listC, limit))


# #### Task 4

# In[45]:


import math

def f(x, mod):
    f = ((math.pow(x,2) + 1) % mod)
    return f


def pollardRho(number):
    x = 1
    y = 1
    d = 1
    iterations = 0

    while d == 1:
        x = f(x, number)
        y = f(f(y, number), number)
        d = gcd(x - y, number)
        iterations += 1
    if d == number: 
        return -1
    else:
        return int(d), iterations


# In[57]:


a, iterA = pollardRho(851)
b, iterB = pollardRho(1517)
c, iterC = pollardRho(31861)
      
print('a) Finner faktor ({}), etter {} iterasjoner.'.format(a, iterA))
print('b) Finner faktor ({}), etter {} iterasjoner.'.format(b, iterB))
print('c) Finner faktor ({}), etter {} iterasjoner.'.format(c, iterC))


# #### Task 5a
# 
# $ M\ =\ m_1\ *\ m_2 $  
# 
# $ e_k(M)\ mod\ n\ =\ e_k(m_1)\ * e_k(m_2)\ mod\ n$  
# 
# Vi vet at å kryptere teksten M mod n gir oss 'C'.   
# Formelen sier at vi kan også finne 'C' ved å dele opp 'M' i  delene 'm1' og 'm2',    
# krypterer dem hver for seg slik at vi finner 'c1' og 'c2', for til slutt å finne C     
# ved å løse: C = c1 * c2 mod n.  
# 
# Viser med å kryptere M = 42 i et eksempel under.
# 
# 
# 
# Eksempel for både oppgave a) :

# In[47]:


import math

p = 137 
q = 139 
e = 5

M = 42 #8
m1 = 6 #4
m2 = 7 #2

n, e, d= rsa_create_keys(p,q,e)

C = rsa_encrypt(M,n,e)
c1 = rsa_encrypt(m1,n,e)
c2 = rsa_encrypt(m2,n,e)


print('5a)\n   {} = {} * {}\n   Krypterer {} til {}\n   Krypterer {} til {}\n   Krypterer {} til {}'.format(M,m1,m2,M,C,m1,c1,m2,c2))
print('\n   Utregning:\n   {} kryptert mod {}: {} % {} = {}'.format(M,n,C,n,(C%n)))
print('   {} kryptert * {} kryptert mod {} = ({} * {}) % {} = {}'.format(m1,m2,n,c1,c2,n,(c1*c2)%n))


# #### Task 5b
# RSA er usikkert mot valgt chiffertekst-angrep.  
# Med noen få utregninger kan en angriper lett finne tilbake til orginalmelding M.
# 
# Eksempel oppgave b:

# In[63]:


import math

p = 137 
q = 139 
e = 5

n, e, d= rsa_create_keys(p,q,e)

cipherText = rsa_encrypt(M,n,e)
attackedCipherText = int((math.pow(2, e) * C) % n)
attackedCipherTextDecrypt = int(rsa_decrypt(attackedCipherText, d, n))
decryptedM = int(attackedCipherTextDecrypt/2)

print('\n5b)\n   Demo: Finner meldingen M med chiffertekst-angrep:')
print('   M = {}\n   n = {}\n   e = {}\n   d = {}'.format(M,n,e,d))
print('\n   cipherText = rsa_encrypt(M,n,e)\n   cipherText =', cipherText)
print('\n.  En angriper kommer over cipher - teksten og angriper den med et chiffettekst-angrep:')
print('\n   attackedCipherText = (2^(e) * cipherText) % n\n   attackedCipherText =', attackedCipherText)
print('\n   attackedCipherTextDecrypt = rsa_decrypt(attackedCipherText, d, n)\n   attackedCipherTextDecrypt =', attackedCipherTextDecrypt)
print('\n   Angriper vet at attackedCipherTextDecrypt = 2*M.')
print('   Angriper finner M.\n   M = attackedCipherTextDecrypt/2 = {}/2 = {}'.format(attackedCipherTextDecrypt, decryptedM))


# #### Task 6a
# 
# ###### Oppgave:  
# Forklar hvorfor vi kan skrive q − p = 2d, hvor d er et heltall.
# 
# ###### Svar:  
# Både p og q er primtall større enn 2, hvor q > p. Det betyr også at p er oddetall.      
# 
# Uttrykker p og q på formen:   
# - p = 2k + 1
# - q = 2k + 1 + a, hvor a er et vilkårlig partall. 
# 
# $ q\ -\ p\ =\ 2d$    
# $ (2k + 1 + a)\ -\ (2k + 1)\ =\ 2d$  
# $ a\ =\ 2d $
# 
# Ettersom a/2 vil alltid gi et heltall må d være et heltall. Likningen stemmer.  
# 
# Eksempel:
# 
# p = 7, q = 11
# 
# $ q\ -\ p\ = 2d$
# $ 11\ -\ 7\ = 2d$  
# $ 4\ = 2d$  
# $ d\ = \ 2$
# 
# 
# #### Task 6b  
# 
# At n + d<sup>2</sup> er et kvadrattall vil si at det finnes et tall x slik at:  
# x * x = n + d<sup>2</sup>
# 
# $ \sqrt{n + d^2}\ = {x^2}$  
# $ \sqrt{n} + d\ +\sqrt{n} + d\ = {x^2}$  
# $ x\ = \sqrt{n} + d$
# 
# Viser med et eksempel:  
# 
# Vi prøver med n = 9 og d = 1
# 
# $ \sqrt{n + d^2}\ = {x^2}$     
# $ \sqrt{9 + 1^2}\ = {x^2}$    
# $ \sqrt{9} + 1\times \sqrt{9} + 1\ = {x^2}$  
# $ (3 + 1)\times (3 + 1) = {x^2}$    
# $ {x^2} = 16$    
# $ x = 4$
# 
# Som vi ser er 16 et kvadrattall fordi 4 * 4 = 16. 
# 
# #### Task 6c
# n kan faktoriseres på følgende måte:  
# 
# $ n + {d^2} = {x^2}$  
# $ n = {x^2} - {d^2}$  
# $ n = (x + d)\times (x-d)$  
# 
# Om q > p, vil p og q se sånn her ut:  
# $ n = q \times p$  
# $ q = x + d$  
# $ p = x - d$  
# 
# #### Task 6d
# 
# n = 152416580095517
# 
# $ \sqrt{n + d^2} = {x^2} $  
# $ x = \sqrt{n} + d $  
# 
# Finner x :   
# Ettersom n er et stort tall og d er et lite tall finner vi x   
# ved å ta kvadratroten av n og runde av til nærmeste hele tall.  
# $ x = \sqrt{n} = \sqrt{152416580095517} = 12345710.999999838 ≈ 12345711$  
# $ x ≈ 12345711$
# 
# Prøver med d = 2
# 
# $ n = q \times p$  
# $ n = (x + d) \times (x - d)$  
# $ n = (12345710 + 2) \times (12345710 - 2)$  
# $ n = 12345711 \times 12345709$  
# $ n = 152416580095517$ 
# 
# Vi ser at vi finner tilbake til n. Det betyr at p og q stemmer.
# ###### Svar:
# n faktorisert:  
# $n = 12345709 \times 12345713$
# 
# Utregning:

# In[52]:


import math

n = 152416580095517
d = 0
x = math.sqrt(n)
x = round(x)

for i in range(1,10):
    res = (x*x) - (i*i)
    if res == n:
        d = i        
        print('x = {}\nd = {}'.format(x,d))        
        print('n = (x+d)(x-d)\nn = ({}+{})({}-{})'.format(x,d,x,d))        
        print('\nFaktoriseringen av n gir:\nn = {} * {}'.format((x+d),(x-d)))
        print('n = {}'.format(res))
        break

