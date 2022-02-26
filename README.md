#Introduction:
In this assignment, a Ransomware is built by me. Through this document I will give your report of 
how to run ransomware and successfully, and then how to decrypt the encrypted fille by 
Ransomware.
This ransomware code is written is Linux but can also be written in windows. However, this 
documentation for Linux.


#Pre-Requirement:
Before, we build have Ransomware, you must install the cryptography module for your python 
interpreter. To do this execute the following command in your Terminal:

pip3 install cryptography


We also need the public and private key for our building our Ransomware. Public key is needed for 
encrypting our key through which we encrypt our file, and private key is needed for decrypting our 
key so that our can decrypt the file which we encrypted through Ransomware. To generate these 
public and private keys, open your terminal and types the following commands:

openssl genrsa -out pub_priv_pair.key 1024

This will generate the private key for us. Through this private key we will now extract our public key. 
Type the following command to do so:

openssl rsa -in pub_priv_pair.key -pubout -out public_key.key

We are all set to go.

#Encrypting the file through Ransomware:

Execute the python script clientCode.txt given by submission by typing the command:

python3 .\clientCode.txt

Note: In the clientCode.txt make sure you have necessary files used for File IO in code with correct 
file paths. If not so modify the clientCode.txt File IO code according to your requirements.

You will see this code will encrypt the file FileToEncrypt.txt.
• FileToEncrypt.txt Before executing Script:
Hello there
• FileToEncrypt.txt After executing Script
gAAAAABiAIfZ80mJPfkgZqjJSPJmVNMWJpsEeZMThWcEI7CXMaD_3vhg3ONZYfN_rDT6KObKNrQUo8RNJAqVSaEHklR5rJOJQ==

#Decrypting the file:
To decrypt the file please run your server by executing serverCode.txt file code.

Python3 .\ServerCode.txt

Then run your extended_client_code.txt file you will see your encrypted file have gotten decrypted 
after the execution of your code.

Python3 .\extended_client_code.txt

After running this your FileToEncrypt.txt will look like:
Hello there






That's it