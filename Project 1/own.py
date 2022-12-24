# -*- coding: utf-8 -*- 
# Shift Cipher Implementation 
# First, the alphabet used by plaintext and ciphertext 
 
abet = 'abcdefghijklmnopqrstuvwxyz' 
 
def enc_shift(k, plaintext): 
    outciph = '' 
    for ctr in plaintext.lower(): 
        try: 
            i = (abet.index(ctr) + k)  % 26 
            outciph += abet[i] 
        except ValueError: 
            outciph += ctr 
    return outciph.lower() 
 
plaintext = 'Alice was beginning to get very tired of sitting by her sister' 
ciphertext = enc_shift(3,plaintext) 
print(ciphertext) 
print(abet.index('j'))
print(ciphertext.upper())
x = 'Rutgers beat '
x += 'Michigan State'
print(x)


def dec_shift(k, ciphertext): 
    outciph = '' 
    for ctr in ciphertext.lower(): 
        try: 
            i = (abet.index(ctr) + k)  % 26 
            outciph += abet[i] 
        except ValueError: 
            outciph += ctr 
    return outciph.lower() 

ciphertext = 'DOLFH ZDV EHJLQQLQJ WR JHW YHUB WLUHG RI VLWWLQJ EB KHU VLVWHU' 
plaintext = enc_shift(-3,ciphertext) 
print(plaintext.capitalize()) 
    
