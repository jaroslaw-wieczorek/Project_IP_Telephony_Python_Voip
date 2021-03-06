from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256 
from base64 import b64encode, b64decode 




class Validator():
    
    def __init__(self, path_private_key : str, path_public_key : str):
        self._private_key = open(path_private_key, "r").read()
        self._public_key = open(path_public_key, "r").read()
    

    def signData(self, msg: str):        
        dataToSign = str(msg)
        print(dataToSign)
    
        priv_key = RSA.importKey(self._private_key) 
        signer = PKCS1_v1_5.new(priv_key) 
        newHash = SHA256.new()
        # It's being assumed the data is base64 encoded, so it's decoded before updating the digest 
        newHash.update(dataToSign.encode("utf-8"))
        return signer.sign(newHash)
   

    def verifyData(self, msg: str, signature):
        dataToVerify = (msg)
        print(dataToVerify)
        
        #public key for tests
        publ_key = RSA.importKey(self._public_key) 
        signer = PKCS1_v1_5.new(publ_key)
        newHash = SHA256.new()
        
        newHash.update(dataToVerify.encode("utf-8"))
        return signer.verify(newHash, signature)
