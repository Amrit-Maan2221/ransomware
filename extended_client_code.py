# Programmer: Amritpal Singh
# Date: 6 February, 2022
# FileName: extended_client_code.txt
# Description: Based on Advanced Computer Security Assignment 1
"""Decrypting the encrypted file here"""



#Now Extending the client Code



#importing some modules
import socket
from cryptography.fernet import Fernet

HOST, PORT = "", 8000

#sending encryted file to the server
def sendEncryptedKey(eKeyFilePath):
    with socket.create_connection((HOST, PORT)) as sock:
        with open(eKeyFilePath, "rb") as file:
            encryptedSymmetricKey = file.read()
            print(encryptedSymmetricKey)
            sock.sendall(encryptedSymmetricKey)
        received = str(sock.recv(1024).decode())

    return received

#decrypting the file
def decryptFile(filePath, key):
    FernetInstance2 = Fernet(key.encode())
    #opening the encrypted file
    with open(filePath,"r") as file:
        decrypted_data = FernetInstance2.decrypt(bytes(file.read(), "utf-8"))
        print(decrypted_data.decode())
        #writing the decrypted data on the file
        with open(filePath, "w") as file_key:
            file_key.write(decrypted_data.decode())

decrptedSymmerticKey = sendEncryptedKey("encryptedSymmertricKey.key")

decryptFile("FileToEncrypt.txt", decrptedSymmerticKey)

