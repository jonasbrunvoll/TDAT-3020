#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
# Needed functions
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

def findLog(base, Beta, mod):
    log = -1 
    for power in range(20):
        x = modularExponentiation(base, power, mod)
        if x == Beta:
            log = power
            break
    return log        

#Test        
#print(findLog(13, 29, 37))


# In[2]:


import numpy as np
import math 

def findOrders(z):
    tot = []
    alphas = []
    powers = []
    for alpha in range(2, z):
        for power in range(1, z):
            num = modularExponentiation(alpha, power, z) 
            if num == 1:
                newElement = [alpha, power]
                tot.append(newElement)
                break
    return tot 


def taskB():
    z = 11
    tot = findOrders(z) 
    matrix = np.chararray((z - 2, z - 1),unicode=True)
    for alpha in range(2,z):
        for beta in range(1, z):
            log = findLog(alpha,beta,z)
            if log == -1: 
                matrix[alpha-2][beta-1] = 'x'
            else:
                matrix[alpha-2][beta-1] = log
            
    return matrix      

z = 11
tot = findOrders(z)
print('\nTask 1.1\n[Alpha, power] = {}.'.format(tot))


matrix = taskB()
print('\nTask 1.2\n\n[Alpha, Beta] --> Matrix:\n {}'.format(matrix))


# In[3]:


#Task 2
def findFirstPrimitivRoot(z):
    orders = findOrders(z)
    for root in orders:
        if (root[1] == z-1):
            return root[0]

        
def findAllPrimitivRoots(z):
    roots = []
    orders = findOrders(z)
    for root in orders:
        if (root[1] == z-1):
            roots.append(root[0])
    return roots 

def countRoots(roots):
    countRoots = 0
    for root in roots: 
        countRoots += 1
    return countRoots
    


# In[4]:


z = 41  
roots = findAllPrimitivRoots(z)
countRoots1 = countRoots(roots)
countRoots2 = countRoots(roots)


print('\nTask 2.1\nPrimitivroots to {}: {}'.format(z,roots))
print('\nTask 2.2\nPrimitivroots to {}: {}'.format('?','?'))
print('\nTask 2.3\nPrimitivroots to {}: {}'.format('?','?'))
print('\nTask 2.4\nAmount of primitiv roots in {}: {}'.format(z,countRoots2))


# In[133]:


#Task 3
import math

def compare(a,b):
    res = 0
    status = True
    while status:  
        for i in range(len(a)-1):
            if not status: break
            for j in range(len(a)-1):
                if a[i] == b[j]:
                    res = a[i]
                    status = False
                    break
    return res

def shanks():
    alpha = 11
    beta = 16 
    p = 29
    lenM = math.ceil(math.sqrt(p))
    m1 = []
    m2 = []
    
    for i in range(lenM - 1):
        e = i*lenM   
        num = modularExponentiation(alpha,e, p) 
        m1.append(num)
    print(m1)
    
    
    gcd, alphaInv, y = gcdExtended(alpha, p)
    
    prevNum = beta
    for i in range(lenM-1):
        if i == 0:
            m2.append(prevNum)
        num = modularExponentiation((prevNum * alphaInv), 1, p)
        m2.append(num)
        prevNum = num
    
    print(m2)
    
    
    r = compare(m1,m2)
    print(r)
    
    


    
    
shanks()  


# In[140]:


#Task 4
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

    
def rsa_encrypt(messege, n, e):
    c = modularExponentiation(messege, e, n)
    return c 
    
def rsa_decrypt(c, d, n):
    messege = modularExponentiation(c, d, n)
    return messege


def rsa_verify(messege, public_key):
    x, y = messege
    n, b = public_key[0], public_key[1]
    res = rsa_encrypt(y,n,b)
    print(res)
    
    



# main
messege_bob_1, messege_bob_2 =  (78,394), (123,289) 

p = 23
n = 437
b = 13
q = 19
public_key = [n, b]
privat_key = 61


rsa_verify(messege_bob_1,public_key)
rsa_verify(messege_bob_2,public_key)


#Bob har satt og RSA-signering med n = 437 og b = 13 som offentlig nøkkel, 
#og p = 23,q = 19,a = 61 som privat nøkkel.


# In[111]:


#Task 5

# ElGamal signering 13^15 mod 37

# p = 37, alpha = 13, beta = 29
# log(3) 29 = 15, fordi 13^15 => 29 mod 37. 

#1
# offentlig nøkkel --> (p, alpha, beta) = (37, 13, 29)
# privat nøkkel --> (p, alpha, log(3) 29) = (37, 13, 15)

#2
def ElGamalEncrypt(k, pub_key, plainText):
    mod = pub_key[0]
    alpha = pub_key[1]
    beta = pub_key[2]
    
    alphaPowerK = modularExponentiation(alpha, k, mod)
    betaPowerK =  modularExponentiation(beta, k, mod)
    xBetaPowerK = modularExponentiation((plainText * betaPowerK), 1, mod)
    return alphaPowerK, xBetaPowerK
    

def ElGamalDecrypt(pub_key, priv_key, signed_messege): 
    mod = pub_key[0]
    alpha = pub_key[1]
    beta = pub_key[2]
    log = priv_key[2]
    alphaPowerK = signed_messege[0]
    xBetaPowerK = signed_messege[1]
    
    a = modularExponentiation(alphaPowerK, log, mod)
    gcd, x, y = gcdExtended(a, mod)
    while x < 0: x += mod
    messege = modularExponentiation(xBetaPowerK * x, 1, mod)
    return messege


plainText, plainText2 = 14, 3
k, k2 = 11, 5
alpha = 13
beta = 29
mod = 37 
log = findLog(alpha, beta, mod)
pub_key = [mod, alpha, beta]
priv_key = [mod, alpha, log]

signed_messege = ElGamalEncrypt(k, pub_key, plainText)
msg_dec = ElGamalDecrypt(pub_key, priv_key, signed_messege)

signed_messege2 = ElGamalEncrypt(k2, pub_key, plainText2)
msg_dec2 = ElGamalDecrypt(pub_key, priv_key, signed_messege2)

print('ElGamalEncrypt: {}'.format(signed_messege))  
print('ElGamalDecrypt: {}'.format(msg_dec))
print('ElGamalEncrypt: {}'.format(signed_messege2))  
print('ElGamalDecrypt: {}'.format(msg_dec2))


# Task 3 
#Bob mottar meldingene 32 med signatur (19,6) og 9 med signatur (32, 16), 
#som skal være fra Alice. Er signaturene gyldige?

recived_msg, recived_msg2  = 32, 9
resived_signature, resived_signature2 = [19, 6], [32, 16]

recived_msg_dec = ElGamalDecrypt(pub_key, priv_key, resived_signature)
recived_msg_dec2 = ElGamalDecrypt(pub_key, priv_key, resived_signature2)


print('Vi finner meldingen {} og {} når vi dekrypterer signaturene. Det er derfor ikke mulig at meldingene {} og {} stemmer.'.format(recived_msg_dec, recived_msg_dec2, recived_msg, recived_msg2))


# In[ ]:





# In[ ]:



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

