import base64
import numpy as np


# input:    numpy array
# output:   string
def encode(obj):
    return base64.b64encode(obj.tobytes()).decode("utf-8")


# input:    string
# output:   numpy array
def decode(obj):
    return np.array(bytearray(base64.b64decode(obj.encode("utf-8"))))


# input:    bytes
# output:   string
def encodeRSA(byt):
    return base64.b64encode(byt).decode("utf-8")


# input:    string
# output:   bytes
def decodeRSA(obj):
    return base64.b64decode(obj.encode("utf-8"))