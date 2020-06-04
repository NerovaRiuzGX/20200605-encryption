import numpy as np
import Substring as SUBSTRING
import Keysort as KEYSORT
import KeyXOR as KEYXOR
import Bitplane as BITPLANE
import Base64Conversion as BASE64

path = {
        0: [BITPLANE, KEYSORT, KEYXOR, SUBSTRING],
        1: [BITPLANE, SUBSTRING, KEYXOR, KEYSORT],
        2: [KEYXOR, KEYSORT, BITPLANE, SUBSTRING],
        3: [KEYXOR, SUBSTRING, BITPLANE, KEYSORT],
        4: [KEYSORT, BITPLANE, SUBSTRING, KEYXOR],
        5: [SUBSTRING, BITPLANE, KEYSORT, KEYXOR],
        6: [KEYSORT, KEYXOR, SUBSTRING, BITPLANE],
        7: [SUBSTRING, KEYXOR, KEYSORT, BITPLANE]
    }

# input: numpy array
# output: int
def generate_path(key):
    path = 0
    for i in range(key.size):
        path = ((path ^ key[i]) >> 1) & 255

    return (path % 8)


# input: string, string
# output: string
def encrypt_engine(source, key):
    src_arr = np.array(bytearray(source, 'utf-8'))
    key_arr = np.array(bytearray(key, 'utf-8'))

    current_path = generate_path(key_arr)

    for algo in path[current_path]:
        src_arr = algo.encrypt(src_arr, key_arr)

    return BASE64.encode(src_arr)


# input: string, string
# output: string
def decrypt_engine(source, key):
    src_arr = BASE64.decode(source)
    key_arr = np.array(bytearray(key, 'utf-8'))

    current_path = generate_path(key_arr)

    for algo in path[current_path][::-1]:
        src_arr = algo.decrypt(src_arr, key_arr)

    return str(src_arr.tobytes(), "utf-8")