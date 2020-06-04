import numpy as np


# input: numpy array
def encrypt(obj, *thing):
    encode_recursion(obj, 0, obj.size)
    reverse(obj, 0, obj.size)
    return obj


# input: numpy array
def decrypt(obj, *thing):
    reverse(obj, 0, obj.size)
    decode_recursion(obj, 0, obj.size)
    return obj


def reverse(obj, start, end):
    if (end-start <= 1):
        return
    obj[start:end] = obj[start:end][::-1]


def encode_recursion(obj, start, end):
    if (end-start <= 1):
        return
    flag = obj[start]
    flag_index = start
    index = flag_index
    while ( index < end ):
        if ( index == end - 1 or obj[index + 1] == flag ):
            reverse(obj, flag_index + 1, index + 1)
            encode_recursion(obj, flag_index + 1, index + 1)
            flag_index = index + 1

        index += 1


def decode_recursion(obj, start, end):
    if (end-start <= 1):
        return
    flag = obj[start]
    flag_index = start
    index = flag_index
    while (index < end):
        if ( index == end - 1 or obj[index + 1] == flag ):
            decode_recursion(obj, flag_index + 1, index + 1)
            reverse(obj, flag_index + 1, index + 1)
            flag_index = index + 1

        index += 1