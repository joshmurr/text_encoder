#!/uer/bin/python
# -*- coding: utf-8 -*-

# Text Encryptor -- by Josh Murr

from random import randint

everything = []

def makeEverything():
    for i in range(32,127):
        everything.append(chr(i))

def generateKey(a, n):
    key = []
    for i in range(n):
        key.append(ord(a[randint(0,len(a)-1)])-32)
    return key

def convertKey(key):
    converted = []
    for i in range(len(key)):
        converted.append(chr(key[i]+32))
    converted = "".join(converted)
    return converted

def encrypt(word, key):
    encryption = []
    final = []
    for i in range(len(word)):
        encryption.append(ord(word[i])-32)
    for i in range(len(encryption)):
        encryption[i] += key[i]
        encryption[i] %= len(everything)
        encryption[i] = chr(encryption[i]+32)
    return "".join(encryption)

def decrypt(eText, key):
    encryptedText = []
    final = []
    thisKey = key
    for i in range(len(eText)):
        encryptedText.append(ord(eText[i])-32)
    for i in range(len(encryptedText)):
        new = encryptedText[i]-thisKey[i]
        new %= len(everything)
        final.append(chr(new+32))
    return "".join(final)

def main():
    makeEverything()
    word = raw_input('Enter some text to encrypt: ')
    key = generateKey(everything, len(word))
    encryption = encrypt(word, key)
    ck = convertKey(key)
    decryptedText = decrypt(encryption, key)
    print "Text = " + word
    print "Key = " + ck
    print "Encryption = " + encryption
    print "Decrypted text = " + decryptedText

if __name__ == '__main__':
    main()