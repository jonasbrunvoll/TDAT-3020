#!/usr/bin/env python
# coding: utf-8

# ## Exercise 16

# Task 1

# In[50]:


import numpy as np
import math

def LSFR_a(K, modN):
    key = str(K)
    firstBin = key
    counter = 0;
    
    while (True):
        key += str(
            (int(key[counter]) + int(key[counter + 1]) + int(key[counter + 2]) + int(key[counter + 3])) % modN)
        try:
            periode = key.index(firstBin, len(K))
            return (key, periode)
        except:
            pass
        counter += 1
       
        
def LSFR_b(K, modN):
    key = str(K)
    firstBin = key
    counter = 0;

    while (True):
        key += str((int(key[counter]) + int(key[counter + 3])) % modN)
        try:
            periode = key.index(firstBin, len(K))
            return (key, periode)
        except:
            pass

        counter += 1


# In[51]:


k1 = '1000'
k2 = '0011'
k3 = '1111'
mod = 2

a1 =  LSFR_a(k1, mod)
a2 =  LSFR_a(k2, mod)
a3 =  LSFR_a(k3, mod) 
b1 =  LSFR_b(k1, mod)
b2 =  LSFR_b(k2, mod)
b3 =  LSFR_b(k3, mod)

print('a1): Pattern: ',a1[0],' Periode:', a1[1])
print('a2): Pattern: ',a2[0],' Periode:', a2[1])
print('a3): Pattern: ',a3[0],' Periode:', a3[1])
print('b1): Pattern: ',b1[0],' Periode:', b1[1])
print('b2): Pattern: ',b2[0],' Periode:', b2[1])
print('b3): Pattern: ',b3[0],' Periode:', b3[1])


# Task 2

# In[4]:


def alph():
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'
    return alph;


def charToNum(char):
    arr = alph()
    for i in range(len(arr)):
        if char == arr[i]:
            return i
    

def numToChar(num):
    arr = alph()
    for i in range(len(arr)):
        if num == i:
            return arr[i]
    

def autoKey_encrypt(plainText, k):
    enc_messege = ''
    textNumbers = []
    cipherNumbers = []
    
    cipherNumbers.append(k)
    
    for i in range(len(plainText)):
        textNumbers.append(charToNum(plainText[i]))
        if i > (len(plainText) - 2):
            break
        else:
            cipherNumbers.append(charToNum(plainText[i]))
         
    for i in range(len(plainText)):
        enc_messege += numToChar((textNumbers[i] + cipherNumbers[i]) % len(alph()))
        
    return enc_messege
   

def autoKey_decrypt(messegeNumbers, k):
    dec_messege = ''
    cipherNumbers = []
    
    cipherNumbers.append(k)
    
    for i in range(len(messegeNumbers)):
        dec_messege += numToChar((messegeNumbers[i] - cipherNumbers[i]) % len(alph()))
        
        if i > (len(messegeNumbers) - 2):
            break
        else:    
            cipherNumbers.append((messegeNumbers[i] - cipherNumbers[i]) % len(alph()))
        
    return dec_messege 
  
    
        
 


# In[6]:


k1 = 17
k2 = 5
text = 'GODDAG'
arr = [23, 8, 23, 12, 21, 2, 4, 3, 17, 13, 19]

enc_messege = autoKey_encrypt(text, k1)
dec_messege = autoKey_decrypt(arr,k2)

print('Encryption of', text, ': =>',enc_messege)
print('Decryption of arr :    =>',dec_messege)


# Task 3
# 

# In[172]:


import math
import numpy as np

def concat(a,b):
    num = a+b
    return num
    
def h(m):
    newnum = ''
    num = bin(int(math.pow(int(m,2), 2) % math.pow(2,8))).replace("0b", "")
    
    if len(num) == 0:
        num += '00000000'
    elif len(num) == 1:
        num += '0000000' + num
    elif len(num) == 2:
        num += '000000' + num
    elif len(num) == 3:
        num += '00000' + num
    elif len(num) == 4:
        num += '0000' + num
    elif len(num) == 5:
        num += '000' + num    
    elif len(num) == 6:
        num += '00' + num
    elif len(num) == 7:
        num += '0' + num 
        
    newnum = num[2]+num[3]+num[4]+num[5]
    return newnum
    
    

def HMAC(k, m):
    K = int(k, 2)
    ipad = 3
    opad = 5
    inner_key = bin(K ^ ipad).replace("0b", "")
    outer_key = bin(K ^ opad).replace("0b", "") 
    inner_hash = h(concat(inner_key, m))
    hmac = h(concat(outer_key, inner_hash))
    return hmac

        


# In[180]:


# a
m = '0110'
k = '1001' 
hash = HMAC(k,m)
print('a) Melding', m, 'genrerer hash', hash, '.')

# b
m2 = '0111'
hash2 = HMAC(k,m2) 
print('b) Melding', m2, 'genrerer hash', hash2, '.')
print('   Vi kalkulerer oss frem til den samme hash verdin som ble sendt med,',hash2,  
      '\n   når vi bruker m =',m2, 'og k =',k,'som input. Det er derfor ingen grunn',
      '\n   til å tro at mldingen ikke er autentisk.')





# Task 4

# In[41]:


import math
import numpy as np

def CBC_MAC(x):
    x = x.split()
    y = int('0000', 2)
    answer = []
    for block in x:
        y = int(((int(y) ^ int(block, 2)) + 3) % math.pow(2, 4))
        answer.append(y)    
    print('CBC-MAC-CÆSAR:', answer)
            
    
x  = '1101 1111 1010 0001' 
x1 = '0010 1100 0001 1111'
CBC_MAC(x) 
CBC_MAC(x1)    


# Task 4

# In[117]:


import math
import numpy as np
from collections import deque

sbox = [
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

inv_s_box = [
            0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
            0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
            0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
            0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
            0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
            0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
            0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
            0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
            0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
            0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
            0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
            0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
            0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
            0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
            0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
]
 
def decimalToHex(num):
    num = hex(int(str(num), 10)).replace("0x", "").upper()
    while len(num) < 2:
        num = '0' + num     
    return num
        
def hexToBinary(text):
    text = text.replace(" ", "")
    # Code to convert hex to binary 
    res = str("{0:08b}".format(int(text, 16))).upper()  
    # If needed add '0' infornt to get the rigth length of text 
    while len(res) / 4 < len(text):
        res = '0' + res     
    return res
   
def binaryToHex(text):
    hexnum = hex(int(text, 2)).replace("0x", "") 
    
    while len(hexnum) * 4 < len(text):
        hexnum = '0' + hexnum 
    return hexnum

def ADDROUNDKEY(text, key): 
    l = len(key)
    text = int(text,2)
    key = int(key,2)
    u = bin(text ^ key).replace("0b", "")
    
    while len(u) < l:
        u = '0' + u  
    return u
    
    
def SUBBYTES(byte):    
    # Divid byte in column and row
    column = byte[0]
    row = byte[1]
    
    #Convert to decimal integers
    columnNum = int(hexToBinary(column), 2)
    rowNum = int(hexToBinary(row), 2)
    
    #Divide sbox into column list.
    columnsInSbox = [sbox[x:x+16] for x in range(0, len(sbox), 16)]
    #Finding the right column
    column = columnsInSbox[columnNum]
    
    subByte = ""
    for i in range(len(column)):
        subByte = column[rowNum]
    return subByte 


def SUBBYTES_INV(byte):    
    # Divid byte in column and row
    column = byte[0]
    row = byte[1]
    
    #Convert to decimal integers
    columnNum = int(hexToBinary(column), 2)
    rowNum = int(hexToBinary(row), 2)
    
    #Divide sbox into column list.
    columnsInSbox = [inv_s_box[x:x+16] for x in range(0, len(inv_s_box), 16)]
    #Finding the right column
    column = columnsInSbox[columnNum]
    
    subByte = ""
    for i in range(len(column)):
        subByte = column[rowNum]
    
    return subByte 


def SHIFTROWS(arr, arg):
    # arg = 0  -> transform tor matrix
    # arg = -1 -> transform tor matrix and shift rigth
    # arg = 1  -> transform tor matrix and shift left
    
    helplist = []
    rowsInArr = []
    for j in range(4):
        rowsInArr.append([arr[i + j] for i in range(0, len(arr), 4)])

    for num in rowsInArr[0]:
        helplist.append(num)
  
    for i in range(1,4):
        rowToShift = deque(rowsInArr[i])
        if arg == 1:
            rowToShift.rotate(i)
        elif arg == -1:
            rowToShift.rotate(-i)
            
        l = list(rowToShift)
        for j in range(4):
            helplist.append(l[j])
    
    arr = helplist 
    return arr


def BAD_AES_encrypt(key, messege):
    enc_List = []
    key = key.replace(" ", "")
    messege = messege.replace(" ", "")
    
    keyBitList = [key[i:i+2] for i in range(0, len(key), 2)]
    messegeBitList = [messege[i:i+2] for i in range(0, len(messege), 2)]
    
    #ADDROUNDKEY 
    for i in range(16):
        keyBitList[i] = hexToBinary(keyBitList[i])
        messegeBitList[i] = hexToBinary(messegeBitList[i])
        enc_List.append(ADDROUNDKEY( messegeBitList[i] , keyBitList[i]))
        enc_List[i] = binaryToHex(enc_List[i])
    
    #SUBBYTES s-box
    for i in range(16):
        enc_List[i] = SUBBYTES(enc_List[i])
        enc_List[i] = decimalToHex(enc_List[i])
    
    
    #SHIFTROWS
    enc_List = SHIFTROWS(enc_List, -1)
    
    
    return enc_List
 
    
def BAD_AES_decryption(key, enc_messege):
    key = key.replace(" ", "")
    enc_messege = enc_messege.replace(" ", "")
    
    keyBitList = [key[i:i+2] for i in range(0, len(key), 2)]
    messegeBitList = [enc_messege[i:i+2] for i in range(0, len(enc_messege), 2)]
    
    
    
    #SHIFTROWS reverse 
    messegeBitList = SHIFTROWS(messegeBitList, 1)
    
    #SUBBYTES inverse s-box
    for i in range(16):
        messegeBitList[i] = SUBBYTES_INV(messegeBitList[i])
        messegeBitList[i] = decimalToHex(messegeBitList[i])
    
    
    
    keyBitList = SHIFTROWS(keyBitList, 0)

    #ADDROUNDKEY 
    for i in range(16):
        keyBitList[i] = hexToBinary(keyBitList[i])
        messegeBitList[i] = hexToBinary(messegeBitList[i])
        messegeBitList[i] = ADDROUNDKEY(keyBitList[i], messegeBitList[i])
        messegeBitList[i] = binaryToHex(messegeBitList[i])
    
   
    return messegeBitList
    


# In[118]:


key = '67 71 35 c4 ff da e5 ff 1c 54 e1 fd 7f 2e 88 b7'
messege = '24 59 66 0c 99 da 9b 00 d6 55 fd 20 e9 ff 46 95'
enc_messege = '26 FA 83 E7 2D CD 5D B8 C4 DC EB 12 70 CF D6 1E'


a = BAD_AES_encrypt(key, messege)
print('Encrypted messege:\n', a)
b = BAD_AES_decryption(key, enc_messege) 
print('\nDecrypt:\n', b)


# Oppgave 6

# In[207]:


Rcon = [
"0x8d", "0x01", "0x02", "0x04", "0x08", "0x10", "0x20", "0x40", "0x80", "0x1b", "0x36", "0x6c", "0xd8", "0xab", "0x4d", "0x9a", 
"0x2f", "0x5e", "0xbc", "0x63", "0xc6", "0x97", "0x35", "0x6a", "0xd4", "0xb3", "0x7d", "0xfa", "0xef", "0xc5", "0x91", "0x39", 
"0x72", "0xe4", "0xd3", "0xbd", "0x61", "0xc2", "0x9f", "0x25", "0x4a", "0x94", "0x33", "0x66", "0xcc", "0x83", "0x1d", "0x3a", 
"0x74", "0xe8", "0xcb", "0x8d", "0x01", "0x02", "0x04", "0x08", "0x10", "0x20", "0x40", "0x80", "0x1b", "0x36", "0x6c", "0xd8", 
"0xab", "0x4d", "0x9a", "0x2f", "0x5e", "0xbc", "0x63", "0xc6", "0x97", "0x35", "0x6a", "0xd4", "0xb3", "0x7d", "0xfa", "0xef", 
"0xc5", "0x91", "0x39", "0x72", "0xe4", "0xd3", "0xbd", "0x61", "0xc2", "0x9f", "0x25", "0x4a", "0x94", "0x33", "0x66", "0xcc", 
"0x83", "0x1d", "0x3a", "0x74", "0xe8", "0xcb", "0x8d", "0x01", "0x02", "0x04", "0x08", "0x10", "0x20", "0x40", "0x80", "0x1b", 
"0x36", "0x6c", "0xd8", "0xab", "0x4d", "0x9a", "0x2f", "0x5e", "0xbc", "0x63", "0xc6", "0x97", "0x35", "0x6a", "0xd4", "0xb3", 
"0x7d", "0xfa", "0xef", "0xc5", "0x91", "0x39", "0x72", "0xe4", "0xd3", "0xbd", "0x61", "0xc2", "0x9f", "0x25", "0x4a", "0x94", 
"0x33", "0x66", "0xcc", "0x83", "0x1d", "0x3a", "0x74", "0xe8", "0xcb", "0x8d", "0x01", "0x02", "0x04", "0x08", "0x10", "0x20", 
"0x40", "0x80", "0x1b", "0x36", "0x6c", "0xd8", "0xab", "0x4d", "0x9a", "0x2f", "0x5e", "0xbc", "0x63", "0xc6", "0x97", "0x35", 
"0x6a", "0xd4", "0xb3", "0x7d", "0xfa", "0xef", "0xc5", "0x91", "0x39", "0x72", "0xe4", "0xd3", "0xbd", "0x61", "0xc2", "0x9f", 
"0x25", "0x4a", "0x94", "0x33", "0x66", "0xcc", "0x83", "0x1d", "0x3a", "0x74", "0xe8", "0xcb", "0x8d", "0x01", "0x02", "0x04", 
"0x08", "0x10", "0x20", "0x40", "0x80", "0x1b", "0x36", "0x6c", "0xd8", "0xab", "0x4d", "0x9a", "0x2f", "0x5e", "0xbc", "0x63", 
"0xc6", "0x97", "0x35", "0x6a", "0xd4", "0xb3", "0x7d", "0xfa", "0xef", "0xc5", "0x91", "0x39", "0x72", "0xe4", "0xd3", "0xbd", 
"0x61", "0xc2", "0x9f", "0x25", "0x4a", "0x94", "0x33", "0x66", "0xcc", "0x83", "0x1d", "0x3a", "0x74", "0xe8", "0xcb"
]


def rotWord(array):
    new_arr = []
    
    for x in range(0, len(array), 4):
        new_arr.append([array[x], array[x + 1], array[x + 2], array[x + 3]]) 
        
    for x in range(4):
        rowToShift = deque(new_arr[x])
        rowToShift.rotate(3)
        new_arr[x] = list(rowToShift)
    
    return new_arr



def stackBeginningKey(array):
    new_arr = []

    for x in range(0, len(array), 4):
        new_arr.append([array[x], array[x + 1], array[x + 2], array[x + 3]])
    
    
    return new_arr



def keyScheduler(startKey):
    listen = []
    arr = []
    keyColumns = stackBeginningKey(startKey)
    rotWords = rotWord(startKey) 
    
    
    
    count = 0
    while(count < 4):
        if(count == 0):
            column = keyColumns[i]
            word = rotWords[-i + 3]
            for j in range(4):
                column = hexToBinary(column[j])
                word = hexToBinary(word[j])
                print(column[j], '  ', word[j])
                print(decimalToHex(int(column[j], 2) ^ int(word[j], 2)))
                arr.append(decimalToHex(int(column[j], 2) ^ int(word[j], 2)))
        else:
            for i in range(1,3):
                column = keyColumns[i]
                word = rotWords[-1+2]
                for j in range(4):
                 
                column[j]= hexToBinary(column[j])
                word[j] = hexToBinary(word[j])
                print(column[j], '  ', word[j])
                print(decimalToHex(int(column[j], 2) ^ int(word[j], 2)))
                arr.append(decimalToHex(int(column[j], 2) ^ int(word[j], 2)))
        listen.append(arr)
        count += 1
        
     
        

    
key = "2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C".split(" ")

keyScheduler(key)
#print("Generert rundenøkler, kolonner er ord:")
#print(keys)    

