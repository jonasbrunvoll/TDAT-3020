#!/usr/bin/env python
# coding: utf-8

# # Øving 14
# 
# Task 1

# In[1]:


mathProblem = (232 + 22 * 77 - 18*18) % 8 
print("Svar: ", mathProblem)


# 232 + 22 * 77 - 18*18 (mod 8)  
# 8*29 + 6 + 5 - 4      (mod 8)  
# 0 + 26                (mod 8)  
# = 2

# Task 2a

# In[2]:


import numpy as np

def mulitplicationTable(z):
    matrix = np.zeros([z - 1, z - 1])
    for x in range(1, z):
        for y in range(1, z):
            matrix[x-1][y-1] = x*y % z
    return matrix

def findMultiplicativInvers(matrix):
    arr = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[i][j] == 1):
                arr.append([i + 1, j + 1])
    return arr


# TASK 2a
matrix = mulitplicationTable(12)
print("\nTASK 2a\nMulitplication Table:\n\n", matrix)

# TASK 2b
z = findMultiplicativInvers(matrix)    
print("\nTASK 2b\nMultiplicativ Inverses are:\n\n", z)


# Task 2c
# For å gå 1 i en rekke / kolonne må det eksistere et tall i settet som er relativt primisk med mod 12. 
# For å få 0 i en rekke / kolonne kan det ikke eksistere et tall i settet som er relativt primisk med mod 12.  
# Dette er en enten eller situasjon og det er grunnen til at man ikke kan ha 0 og en 1 i samme rad/kolonne.

# Task 3

# In[3]:


import numpy as np


def findDeterminantMatrix(matrix):
    det = int(np.linalg.det(matrix))
    return det

def findInversMatrix(matrix):
    inv = np.linalg.inv(matrix) * np.linalg.det(matrix)
    return inv

def findInversMatrixOver_Z(matrix, z):
    det = findDeterminantMatrix(matrix)
    z_det_mod = det % len(z)
    multiplicativInv_z = findMultiplicativInvers(z)
    det_in_multipl_inverse = False
    
    
    for x in multiplicativInv_z:
        if z_det_mod in x:
            det_in_multipl_inverse = True
            
    if (det_in_multipl_inverse):
        matrixInv = findInversMatrix(matrix)
        return matrixInv
    else:
        return None
       


# In[4]:


arr = np.array([[2, -1], [5, 8]])

z9 = mulitplicationTable(10)
z10 = mulitplicationTable(11)

matrixOverZ10 = findInversMatrixOver_Z(arr, z10)
matrixOverZ9 = findInversMatrixOver_Z(arr, z9)

print('\na) Invers matrix over Z10 does exist:\n', matrixOverZ10)
print('\nb) Invers matrix over Z9: does exist:\n', matrixOverZ9)


# Task 4
# 
# a) Svar: Et enkelt substitusjonsschiffer med et alfabt med 29 tegn kan ha 29 forskjellige    nøkler. Her er vært tegn en perumatasjon av et annet tegn. Eksepel bokstaven 'a' gir 'b' og bokstaven 'b' gir 'k' 
# 
# b) Enkle grep Alice og Bob kan gjøre for å gjøre det vanskligere for Eva å tolke medlingene er å skrive dialekt, droppe vokaler, droppe dobble konsonanter, sende meldinger med utradisjonel settings oppbygging, osv.   
# 
# 
# c) Det finnes n! antall nøkler. Eks: 29! = 8.41761994*10^30. Det er veldig mange mulige nøkler! 
#  

# Task 5

# In[5]:


# Functions
def convertStringToNumbers(messege, alfabet, k):
    numbers = []
    for i in range(len(messege)):
        for j in range(len(alfabet)):
            if messege[i] == alfabet[j]:
                numbers.append((j+k) % len(alfabet))
    return numbers


def convertNumbersToString(numbers, alfabet):
    newmessage = []
    for i in range(len(numbers)):
        for j in range(len(alfabet)):
            if numbers[i] == j:
                newmessage.append(alfabet[j])
    return newmessage


# Task 5
secretMessage = 'YÆVFB VBVFR ÅVBV'
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'

print('-'*40, 'ANSWER', '-'*40)
for k in range(12, 13):
    numbers = convertStringToNumbers(secretMessage, alfabet, k)
    messege = convertNumbersToString(numbers, alfabet)

    # convert 'messege' from array to string
    printMessegeOut = ''
    for i in messege:
        printMessegeOut += i

    print('\nk = ', k, '\nMessege: ', printMessegeOut, '\n')
print('-'*39, 'Finished', '-'*39)


# Task 6
# 
# a) 
# 
# P = mengedne av mulig klartekst
# C = mengden av mulig kryptrt tekst
# K = mengden av mulige nøkler.
# N = antall tegg
# 
# P = C = K = {x| 0 <= x N}
#     en_k(x1, x2 ...., xb) = (x1+k, x2+k...xb+k)(mod N)
#     de_l(x1, x2 ...., xb) = (x1-k, x2-k...xb-k)(mod N)
# 
# b)
# Chiferet kan ha N^B antall forskjellige nøkler, hvor B er blokklengde og N antall mulige tegn. 
#     

# Oppgave 7

# In[13]:


alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"

def findIndex(char):
    for i in range(len(alfabet)):
        if char == alfabet[i]:
            return i

def encryptMessege(messege, key):
    secretMessege = ''
    for i in range(len(messege)):
        messege_pos = findIndex(messege[i])
        key_pos = findIndex(key[i % len(key)])
        secretMessege += alfabet[(messege_pos + key_pos) % len(alfabet)]
    return secretMessege


def decryptMessege(secretmessege, key):
    messege = ''
    for i in range(len(secretmessege)):
        messege_pos = findIndex(secretmessege[i])
        key_pos = findIndex(key[i % len(key)])
        messege += alfabet[(messege_pos - key_pos) % len(alfabet)]
    return messege

# Task 7a
messege = "NÅERDETSNARTHELG"
key = "TORSK"
enryptedMessege = encryptMessege(messege, key)
print('a) : ', enryptedMessege)

# Task 7b
messegeToDecrypt = 'QZQOBVCAFFKSDC'
key2 = "BRUS"
decryptedMessege = decryptMessege(messegeToDecrypt, key2)
print('b) : ', decryptedMessege)




# c) 29^5 = 20511149 antall mulig nøkler med en lengde 5 på nøkkelen

# Task 8

# In[7]:


#Functions

def convertStringToNumbers(messege, alfabet):
    numbers = []
    for i in range(len(messege)):
        for j in range(len(alfabet)):
            if messege[i] == alfabet[j]:
                numbers.append(j)
    return numbers

def numberToChar(num, alfabet):
    charIndex = 0
    for j in range(len(alfabet)):
        if num == j:
            charIndex = num % len(alfabet) 
    return alfabet[charIndex]
    

def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def encrypt_Hill(messege, K_matrix, alph):
    messege_vector = np.array(convertStringToNumbers(messege, alph)).reshape(-1, 2)
    
    chiper = ""
    encryptList = []
    
    for row in messege_vector:
        encryption = (row @ K_matrix)%len(alph)
        encryptList.append(encryption)
    
    for row in encryptList:
        for column in row:
            chiper += numberToChar(column, alph)
        
    return chiper


def decrypt_Hill(messege, K_matrix, alph):
    inv_K_matrix = findInversMatrix(K_matrix)
    messege_vector = np.array(convertStringToNumbers(messege, alph)).reshape(-1, 2)
    
    detK = round(np.linalg.det(k))
    x = gcdExtended(detK, len(alph))[1]
    
    chiper = ""
    decryptList = []
    for row in messege_vector:
        decryption = (row@(invK * x))% len(alph)
        decryptList.append(decryption)
    
    
    for row in decryptList:
        for column in row:
            chiper += (numberToChar(round(column), alph))
        
    
    return chiper

    


# In[9]:


alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'
messege = 'PRIM'
secretMessege = 'NHID'

# Task 8a
k = np.array([[11, 8], [3,7]])
z29 = mulitplicationTable(29)
invK = findInversMatrixOver_Z(k, z29)
print('\nTask 8a: \nK =\n',k, '\n\ninvK =\n', invK)


# Task 8b
s = encrypt_Hill(messege, k, alph)
print('\nTask 8b:\nEncryption er: ',s)


# Task 8c
t = decrypt_Hill(secretMessege, k, alph)

print('\nTask 8b:\nDecryption er:',t)

w = decrypt_Hill('TOYYSN', k, alph)
print('\nTask 8c:\nDecryption er:',w)





# Task 8d er løst på ark.

# In[ ]:




