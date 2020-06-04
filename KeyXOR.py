"""
Created on Wed Jun  3 15:29:36 2020

@author: 林煒堉
"""
import numpy as np

def old_encrypt(msg_np, key_np):
    key_list = []
    msg_list = []

    [key_list.append([key_np[k], list('{0:b}'.format(key_np[k]))]) for k in range(len(key_np))]        
    [msg_list.append(msg_np[k]) for k in range(len(msg_np))]
    backup_key_list = key_list.copy()
    
    #print(key_list[1][1][0])
    #if len(msg_list) < len(key_list):
        #return print("key 比 msg 長")
    
    do_count = len(msg_list) / len(key_list)
    #print(do_count)
    #print(bin(11^5))
    
    msg_iter = 0
    for i in range(int(do_count)):
        msg_iter = i * len(key_list)
        for t in range(len(key_list)):
            key_char = key_list[t][0]
            for p in range(len(key_list[t][1])):
                if key_list[t][1][p] == '1' and msg_iter + t + p < (i + 1) * len(key_list):
                    msg_list[msg_iter + t + p] ^= key_char
                    #print(key_list[t][1])
                    #print(t, p, msg_iter + t + p, msg_list[msg_iter + t + p])
                key_char = (key_char << 1) & 255
    
    #print(msg_list)
    
    msg_end = len(key_list) * int(do_count)
    length = len(msg_list) - msg_end
    
    #print(len(msg_list))
    #print(backup_key_list)
    if length > 0:
        for i in range(len(backup_key_list) - length):
            backup_key_list.pop(-1)
            
        #print(backup_key_list)
        for t in range(msg_end, len(msg_list)):
            for p in range(len(backup_key_list[t % len(key_list)][1])):
                if backup_key_list[t % len(key_list)][1][p] == '1' and t % len(key_list) + p < (len(backup_key_list)):
                    msg_list[t + p] ^= backup_key_list[t % len(key_list)][0]
                    #print(key_list[t][1])
                    #print(t, p, msg_iter + t + p, msg_list[msg_iter + t + p])

    #print(msg_list)
    #print(backup_key_list)
    #print(key_list)
    #print(msg_list)
    encrypt_msg_np = np.array(msg_list, dtype=np.uint8)
    #print(encrypt_msg_np)
    return encrypt_msg_np


def old_decrypt(msg_np, key_np):
    key_list = []
    msg_list = []

    [key_list.append([key_np[k], list('{0:b}'.format(key_np[k]))]) for k in range(len(key_np))]        
    [msg_list.append(msg_np[k]) for k in range(len(msg_np))]
    backup_key_list = key_list.copy()
    
    #print(key_list[1][1][0])
    #if len(msg_list) < len(key_list):
        #return print("key 比 msg 長")
    
    do_count = len(msg_list) / len(key_list)
    #print(key_list)
    #print(bin(11^5))
    
    msg_iter = 0
    for i in range(int(do_count)):
        msg_iter = i * len(key_list)
        for t in range(len(key_list) - 1, -1, -1):
            key_char = key_list[t][0]
            for p in range(len(key_list[t][1])):
                if key_list[t][1][p] == '1' and msg_iter + t + p < (i + 1) * len(key_list):
                    msg_list[msg_iter + t + p] ^= key_char
                    #print(key_list[t][1])
                    #print(t, p, msg_iter + t + p, msg_list[msg_iter + t + p])
                    key_char = (key_char << 1) & 255
    
    #print(msg_list)
    
    msg_end = len(key_list) * int(do_count)
    length = len(msg_list) - msg_end
    
    #print(len(msg_list))
    #print(backup_key_list)
    if length > 0:
        for i in range(len(backup_key_list) - length):
            backup_key_list.pop(-1)
            
        #print(backup_key_list)
        for t in range(len(msg_list) - 1, msg_end - 1, -1):
            for p in range(len(backup_key_list[t % len(key_list)][1])):
                if backup_key_list[t % len(key_list)][1][p] == '1' and t % len(key_list) + p < (len(backup_key_list)):
                    msg_list[t + p] ^= backup_key_list[t % len(key_list)][0]
                    #print(key_list[t][1])
                    #print(t, p, msg_iter + t + p, msg_list[msg_iter + t + p])

    #print(msg_list)
    #print(backup_key_list)
    #print(key_list)
    #print(msg_list)
    encrypt_msg_np = np.array(msg_list, dtype=np.uint8)
    #print(encrypt_msg_np)
    return encrypt_msg_np

def encrypt(msg_np, key_np):
    key_list = []
    msg_list = []

    [key_list.append([key_np[k], format(key_np[k], '08b')]) for k in range(len(key_np))]        
    [msg_list.append(msg_np[k]) for k in range(len(msg_np))]

    for count in range(len(msg_list)):
        key_char = key_list[count % len(key_list)].copy()
        for position in range(8):
            target = position + count
            if (target >= len(msg_list)):
                break

            if (key_char[1][position] == '1'):
                msg_list[target] ^= key_char[0]

            key_char[0] = (key_char[0] << 1) & 255

    return np.array(msg_list, dtype=np.uint8)


def decrypt(msg_np, key_np):
    return encrypt(msg_np, key_np)