from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import Base64Conversion as BASE64
import binascii

def get_key():
    try:
        with open('self_pubKey.pem', "r") as f:
            pk = RSA.importKey(f.read())
        with open('self_prvKey.pem', "r") as f:
            pvk = RSA.importKey(f.read())
        return {
            'pk': pk,
            'pvk': pvk
        }
    except:
        keyPair = RSA.generate(1024)
        pubKey = keyPair.publickey()
        privKeyPEM = keyPair.export_key()
        with open("self_pubKey.pem", "wb") as f:
            f.write(pubKey.export_key('PEM'))
        with open("self_prvKey.pem", "wb") as f:
            f.write(keyPair.export_key('PEM'))
        return {
            'pk': pubKey,
            'pvk': privKeyPEM
        }


# input:    string, string
# output:   string
def encryption(path, plain):
    with open(path, "r") as f:
        other_pk = RSA.importKey(f.read())
    byte_plain = plain.encode('utf-8')
    encryptor = PKCS1_OAEP.new(other_pk)
    encrypted = encryptor.encrypt(byte_plain)

    #print(type(encrypted))

    #with open("cipher.txt", "wb") as f:
    #    f.write(encrypted)
    #print("Encrypted:", encrypted)
    return BASE64.encodeRSA(encrypted)


# input:    string
# output:   string
def decryption(cipher):
    k = get_key()
    cipher_byt = BASE64.decodeRSA(cipher)
    decryptor = PKCS1_OAEP.new(k['pvk'])
    decrypted = decryptor.decrypt(cipher_byt)
    #with open('decryption.txt', "w") as f:
    #    f.write(decrypted.decode())
    #print('Decrypted:', decrypted)

    return decrypted.decode("utf-8")