import Encryption_engine as ENC_ENG
import RSA_engine as RSA_ENG
import QR_engine as QR_ENG
from argparse import ArgumentParser


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-p", "--path", dest="path", type=str, default="Cipher.png", help="The file path of your QR Code.")
    
    args = parser.parse_args()

    [encrypted_text, encrypted_key] = QR_ENG.detect(args.path)

    original_key = RSA_ENG.decryption(encrypted_key)
    print("Original key:  " + original_key)

    original_text = ENC_ENG.decrypt_engine(encrypted_text, original_key)
    print("Original text: " + original_text)