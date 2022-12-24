
To be able to see cryptography and security algorithms in action, you will have to rely on your code 
writing skills. While there are many different magical languages with which to command the great 
computing machine, you and your housemates will be programming in Python.  It is a great language 
with which to tinker around with the fundamentals of security, and it is also a programming language 
that you will find very useful as you go out into the great big world beyond the Kingdom of Rutgers!  
We are going to start with a very simple assignment: you are going to get your feet wet with 
programming a classic cipher in Python.   

Create A Program  
The next part of this lesson/assignment is for you to create your own program for performing the shift 
cipher.  In whatever development environment you choose, make your own .py file that contains the 
following code: 
----------------------------------------------------------------------------------------------------- 
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
 
------------------------------------------------------------------------------------------------------------------------- 
Run this program.  What is the resulting ciphertext output?  Your house is to submit a single pdf file in 
Canvas containing the answers to the problems in this assignment. In the pdf file, the answer to this 
problem should be identified as problem 1. 
 
Learning Some Python: 
For this part of the assignment, we are going to explore some of the variables we have used.  
From the Python command line, find the output of 
>> abet.index(‘j’)  
Your house is to submit a single pdf file in Canvas containing the answers to the problems in this 
assignment. In the pdf file, the answer to this problem should be identified as problem 2. 
Next, from the Python command line, find the output of  
>> ciphertext.upper() 
Your house is to submit a single pdf file containing the answers to the problems in this assignment. In 
the pdf file, the answer to this problem should be identified as problem 3. 
Next, from the Python command line, find the output of  
>> x = ‘Rutgers beat’ 
>> x +=’ Michigan State’ 
>> print(x) 
 
