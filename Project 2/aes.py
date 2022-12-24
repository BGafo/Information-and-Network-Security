from Crypto.Cipher import AES 
iv = b"1223334444555556" 
key = b"abcdabcddcbadbca" 
 
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
