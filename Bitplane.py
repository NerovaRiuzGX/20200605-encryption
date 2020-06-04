"""
Created on Wed Jun  3 18:08:48 2020

@author: 林煒堉
"""
import numpy as np

def encrypt(msg_list, *thing):
    temp = [format(i, '08b') for i in msg_list]
    sum_list = "".join(temp)
    arr_list = ""
    for count in range(8):
        arr_list += sum_list[count:len(sum_list):8]

    return np.array([int(arr_list[8*length:8*length+8], 2) for length in range(msg_list.size)], dtype=np.uint8)
    
def decrypt(msg_list, *thing):
    temp = [format(i, '08b') for i in msg_list]
    sum_list = "".join(temp)
    arr_list = ""
    for count in range(msg_list.size):
        arr_list += sum_list[count:len(sum_list):msg_list.size]

    return np.array([int(arr_list[8*length:8*length+8], 2) for length in range(msg_list.size)], dtype=np.uint8)
