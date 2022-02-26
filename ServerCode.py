# Programmer: Amritpal Singh
# Date: 6 February, 2022
# FileName: ServerCode.txt
# Description: Based on Advanced Computer Security Assignment 1

"""Bascially, here we are receving enrypted Symettric key from client and sending it by decrypting it"""


import socketserver
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class ClientHandler(socketserver.BaseRequestHandler):

    def handle(self):
        #receiving encrypted key from client
        encrypted_key = self.request.recv(1024).strip()
        #opening the private key file
        with open("pub_priv_pair.key", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        #decrypting the symmetric key using private key
        decryptedSymmetricKey = private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        #sending decryptedSymmetric code to client
        self.request.sendall(decryptedSymmetricKey)



if __name__ == "__main__":
    HOST, PORT = "", 8000

    tcpServer =  socketserver.TCPServer((HOST, PORT), ClientHandler)
    try:
        print("Server has started......")
        tcpServer.serve_forever()
    except:
        print("There was an error")