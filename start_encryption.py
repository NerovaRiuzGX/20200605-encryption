import Encryption_engine as ENC_ENG
import RSA_engine as RSA_ENG
import QR_engine as QR_ENG
from argparse import ArgumentParser


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-r", "--rsakey-path", dest="RSAkey_path", type=str, default="other_pk.pem", help="The file path of your Receiver's public key.")
    parser.add_argument("-t", "--text-path", dest="text_path", type=str, default="plain_text.txt", help="The file path of your text for encryption.")
    parser.add_argument("-k", "--key-path", dest="key_path", type=str, default="custom_key.txt", help="The file path of your custom key for encryption.")

    args = parser.parse_args()

    with open(args.text_path, 'r') as f:
        original_text = f.read()

    with open(args.key_path, 'r') as f:
        original_key = f.read()

    encrypted_text = ENC_ENG.encrypt_engine(original_text, original_key)
    print("Encrypted text:  " + encrypted_text)

    encrypted_key = RSA_ENG.encryption(args.RSAkey_path, original_key)
    print("Encrypted key:   " + encrypted_key)

    output_file = QR_ENG.QR_generator(encrypted_text, encrypted_key)
    print("Output filename: " + output_file)