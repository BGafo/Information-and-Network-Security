
Python AES Assignment 
In this assignment, you are going to gain some experience with the AES block cipher, and how to use it in 
different modes of operation.   
Your House should collect answers to all of the problems into one file and submit a pdf file containing 
everything. Inline submissions cannot be used for this assignment because you will submit some 
pictures. Submissions are to be uploaded to the Canvas site. One submission per group. 
Your starting program: Making a Random Key 
To start, enter the following code into your Python environment.  
----------------------------------------------------------------------------------------------------- 
import os 
import binascii 
 
key=binascii.hexlify(os.urandom(16)) 
print ('The Key You Made Was: ', [x for x in key]) 
print('The Key You Made Was: ', key) 
------------------------------------------------------------------------------------------------------------------------- 
Run this code.  What are the answers that you got for the key?  Explain the differences between these 
two answers and why the different answers were produced. Submit the answer as Problem 1.  
 
Saving and Loading that Key: 
It will be very useful to save and later reload an encryption key.  In this part of the assignment, you will 
combine the key generation steps taught above with simple file opening, writing, and reading.  
Enter the following code. 
 
-------------------------------------------------------------------------------------------------------------------------------- 
import os 
import binascii 
 
def write_key(): 
    # Make a random key with 16 bytes 
    key=binascii.hexlify(os.urandom(16)) 
    print ('The Key You Made Was: ', [x for x in key]) 
[{{type}} Annotation]
    with open("scratch.key","wb") as file: 
        file.write(key) 
         
def read_key(): 
    with open("scratch.key","rb") as file: 
        keynew = file.read() 
    return keynew 
 
#Now the main body of the program... 
write_key() 
keys=read_key() 
print ('The Key You Made Was: ', [x for x in keys]) 
----------------------------------------------------------------------------------------------------------------- 
 
Submit the resulting answer for this assignment as problem 2 in your pdf file.  
 
Encrypting with AES and ECB Mode: 
For this part of the assignment, your first step will be to download the file “RutgersLogo.bmp” from  
Canvas and put it under the same directory as your python script. 
To use this file in Colab, upload it to your session storage as shown in the picture. You need to do this 
every time you restart the Colab. 
 
Next, enter the following code. If the Crypto module is missing, install it using pip install pycrypto. In 
Colab, install pycrypto as shown in the picture (!pip install pycrypto). You need to do this every time you 
restart the Colab. 
 
---------------------------------------------------- 
from Crypto.Cipher import AES 
 
key = b"abcdabcdabcdabcd" 
cipher = AES.new(key, AES.MODE_ECB) 
# encrypt using ECB mode 
with open("RutgersLogo.bmp", "rb") as f: 
    byteblock = f.read() 
 
pad = len(byteblock)%16 * (-1) 
byteblock_trimmed = byteblock[64:pad] 
ciphertext = cipher.encrypt(byteblock_trimmed) 
ciphertext = byteblock[0:64] + ciphertext + byteblock[pad:] 
 
with open("RutgersLogoECB.bmp", "wb") as f: 
    f.write(ciphertext) 
 
# decrypt using the reverse process 
with open("RutgersLogoECB.bmp", "rb") as f: 
    byteblock = f.read() 
 
pad = len(byteblock)%16 * -1 
byteblock_trimmed = byteblock[64:pad] 
plaintext = cipher.decrypt(byteblock_trimmed) 
plaintext = byteblock[0:64] + plaintext + byteblock[pad:] 
 
with open("RutgersLogoECB_Dec.bmp", "wb") as f: 
    byteblock = f.write(plaintext) 
 
print ("Done, finished writing and decrypting ECB mode") 
 
------------------------------------------------------------ 
Using the results, answer the following questions. 
Submit your answer to problem 3: Explain what the following lines of code did--- 
pad = len(byteblock)%16 * (-1) 
byteblock_trimmed = byteblock[64:pad] 
ciphertext = cipher.encrypt(byteblock_trimmed) 
ciphertext = byteblock[0:64] + ciphertext + byteblock[pad:] 
 
For the answer to problem 4: Open the “RutgersLogoECB.bmp” file and submit a copy & paste of the 
image.  
 
Encrypting with AES and CBC Mode: 
For this part of the assignment, you will do almost the same as you did in the previous example, but you 
will switch the mode of operation to “CBC”.  Enter the following code: 
 
----- --- -- - -------------------------------------------------------------------- 
from Crypto.Cipher import AES 
iv = b"1111222233334444" 
key = b"abcdabcdabcdabcd" 
 
cipher = AES.new(key, AES.MODE_CBC, iv) 
# encrypt using CBC mode 
with open("RutgersLogo.bmp", "rb") as f: 
    byteblock = f.read() 
 
pad = len(byteblock)%16 * -1 
byteblock_trimmed = byteblock[64:pad] 
ciphertext = cipher.encrypt(byteblock_trimmed) 
ciphertext = byteblock[0:64] + ciphertext + byteblock[pad:] 
 
with open("RutgersLogoCBC.bmp", "wb") as f: 
    f.write(ciphertext) 
 
# decrypt using the reverse process 
 
 
cipher = AES.new(key, AES.MODE_CBC, iv) 
with open("RutgersLogoCBC.bmp", "rb") as f: 
    byteblock = f.read() 
 
pad = len(byteblock)%16 * -1 
byteblock_trimmed = byteblock[64:pad] 
plaintext = cipher.decrypt(byteblock_trimmed) 
plaintext = byteblock[0:64] + plaintext + byteblock[pad:] 
 
with open("RutgersLogoCBC_Dec.bmp", "wb") as f: 
    byteblock = f.write(plaintext) 
print ("done") 
----- --- -- - -------------------------------------------------------------------- 
For the submission to Problem 5: I want each member of your House to run this code, but to change the 
key and the IV. Execute the code and open the “RutgersLogoCBC.bmp” file. Then, I want each member 
of the House to submit an answer to this problem (in the single pdf file that will be submitted), clearly 
labeled with: 
• Each person’s name next to the copy and paste of their own CBC encrypted image. 
• The key and IV that that person used. 
• And submit a copy and paste of the CBC encrypted image as your individual answer to Problem 
5. 
 
For Problem 6, explain why the results for ECB and CBC modes are different. Does ECB mode leak any 
form of information? Which mode should you use?    
 
Putting it Together 
For this part of the assignment, you will use the code examples above to generate a random key and a 
random IV (“initialization vector”), then write that key and IV to a key data file. Then, you will open the 
image file, encrypt it with AES in CBC mode, and save that to a new .bmp file.  Next, you will open the 
key data file, read in the key, and IV. Then, you will open the CBC encrypted .bmp file, and decrypt it 
using the key and IV.  Finally, you will create your own function that checks whether the decrypted 
result is the same as the original image. 
For Problem 7, submit a copy and paste of your code in the pdf file.    
House Internal Verification: 
For this part of the assignment, each person in your House is to verify that at least two other members 
of your House were able to successfully complete the assignment.  To do this, for example, you might 
want to set up a chat session between groups of three and spend 5 to 10 minutes making certain 
everyone could successfully write and run the code. Once a house member has verified two other 
people in their House, they are to add their name to a list of verifiers in problem 8. The submission of 
the pdf file to Canvas should only happen when all members of the group have verified two other 
members and have placed their names as an answer to problem 8. 
 
