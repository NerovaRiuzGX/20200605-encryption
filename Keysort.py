"""
Created on Tue Jun  2 23:15:57 2020

@author: 林煒堉
"""

import numpy as np
"""
key = [7, 2, 8, 3, 6, 6]
msg = [1, 2, 3, 4, 5, 10, 9, 8]

#[23, 16, 8, 2, 1] [7, 2, 8, 3, 6, 6]

key_np = np.array(key)
msg_np = np.array(msg)

#print(msg_np)
"""

def old_encrypt(msg_np, key_np):
    key_list = []
    msg_list = []

    [key_list.append([key_np[k], k, k]) for k in range(key_np.size)]        
    [msg_list.append(msg_np[k]) for k in range(msg_np.size)]
    backup_key_list = key_list.copy()
    #print(backup_key_list)
    for i in range(len(key_list) - 1):
        for j in range(len(key_list) - i - 1):
            if key_list[j][0] > key_list[j + 1][0]:
                temp = key_list[j]
                key_list[j] = key_list[j + 1]
                key_list[j + 1] = temp
                key_list[j + 1][2] = j + 1
                key_list[j][2] = j
                
    #print(key_list)
    
    if len(msg_list) < len(key_list):
        return print("key 比 msg 長")
    
    do_count = len(msg_list) / len(key_list)
    #print(do_count)
    
    msg_iter = 0
    for i in range(int(do_count)):
        msg_iter = i * len(key_list)
        temp = [n for n in range(len(key_list))]
        for t in key_list:
            temp[t[2]] = msg_list[msg_iter + t[1]]
        for k in range(len(key_list)):
            msg_list[k + msg_iter] = temp[k]
    
    msg_end = len(key_list) * int(do_count)
    length = len(msg_list) - msg_end
    
    #print(msg_end)
    #print(backup_key_list)
    if length > 0:
        for i in range(len(backup_key_list) - length):
            backup_key_list.pop(-1)
            
        #print(backup_key_list)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if backup_key_list[j][0] > backup_key_list[j + 1][0]:
                    temp = backup_key_list[j]
                    backup_key_list[j] = backup_key_list[j + 1]
                    backup_key_list[j + 1] = temp
                    backup_key_list[j + 1][2] = j + 1
                    backup_key_list[j][2] = j
        temp = [n for n in range(len(backup_key_list))]
        #print(backup_key_list)
        for t in backup_key_list:
            temp[t[2]] = msg_list[msg_end + t[1]]
        for k in range(len(backup_key_list)):
            msg_list[k + msg_end] = temp[k]
    #print(backup_key_list)
    #print(key_list)
    #print(msg_list)
    encrypt_msg_np = np.array(msg_list)
    #print(encode_msg_np)
    return encrypt_msg_np

def old_decrypt(msg_np, key_np):
    key_list = []
    msg_list = []

    [key_list.append([key_np[k], k, k]) for k in range(key_np.size)]        
    [msg_list.append(msg_np[k]) for k in range(msg_np.size)]
    backup_key_list = key_list.copy()
    #print(backup_key_list)
    for i in range(len(key_list) - 1):
        for j in range(len(key_list) - i - 1):
            if key_list[j][0] > key_list[j + 1][0]:
                temp = key_list[j]
                key_list[j] = key_list[j + 1]
                key_list[j + 1] = temp
                key_list[j + 1][2] = j + 1
                key_list[j][2] = j
                
    #print(key_list)
    
    if len(msg_list) < len(key_list):
        return print("key 比 msg 長")
    
    do_count = len(msg_list) / len(key_list)
    #print(do_count)
    
    msg_iter = 0
    for i in range(int(do_count)):
        msg_iter = i * len(key_list)
        temp = [n for n in range(len(key_list))]
        for t in key_list:
            temp[t[1]] = msg_list[msg_iter + t[2]]
        for k in range(len(key_list)):
            msg_list[k + msg_iter] = temp[k]
    
    msg_end = len(key_list) * int(do_count)
    length = len(msg_list) - msg_end
    
    #print(msg_end)
    #print(backup_key_list)
    if length > 0:
        for i in range(len(backup_key_list) - length):
            backup_key_list.pop(-1)
            
        #print(backup_key_list)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if backup_key_list[j][0] > backup_key_list[j + 1][0]:
                    temp = backup_key_list[j]
                    backup_key_list[j] = backup_key_list[j + 1]
                    backup_key_list[j + 1] = temp
                    backup_key_list[j + 1][2] = j + 1
                    backup_key_list[j][2] = j
        temp = [n for n in range(len(backup_key_list))]
        #print(backup_key_list)
        for t in backup_key_list:
            temp[t[1]] = msg_list[msg_end + t[2]]
        for k in range(len(backup_key_list)):
            msg_list[k + msg_end] = temp[k]
    #print(backup_key_list)
    #print(key_list)
    #print(msg_list)
    decode_msg_np = np.array(msg_list)
    #print(decode_msg_np)
    return decode_msg_np

def encrypt(msg_np, key_np):
    key_list = []
    msg_list = []
    new_msg_list = []

    [key_list.append([key_np[k], k]) for k in range(key_np.size)]        
    [msg_list.append(msg_np[k]) for k in range(msg_np.size)]
    backup_key_list = key_list.copy()

    key_list.sort()

    while (len(msg_list) >= len(key_list)):
        new_msg_tmp = []
        msg_tmp = msg_list[0:len(key_list)]

        for obj in key_list:
            new_msg_tmp.append(msg_tmp[obj[1]])
        
        new_msg_list.extend(new_msg_tmp)
        msg_list = msg_list[len(key_list):]

    if (len(msg_list) > 0):
        backup_key_list = backup_key_list[0:len(msg_list)]
        backup_key_list.sort()

        new_msg_tmp = []

        for obj in backup_key_list:
            new_msg_tmp.append(msg_list[obj[1]])

        new_msg_list.extend(new_msg_tmp)

    #thing = np.array(new_msg_list)
    #print(str(thing.tobytes(), "utf-8"))
    return np.array(new_msg_list, dtype=np.uint8)
    
def decrypt(msg_np, key_np):
    key_list = []
    msg_list = []
    new_msg_list = []

    [key_list.append([key_np[k], k]) for k in range(key_np.size)]        
    [msg_list.append(msg_np[k]) for k in range(msg_np.size)]
    backup_key_list = key_list.copy()

    key_list.sort()

    while (len(msg_list) >= len(key_list)):
        new_msg_tmp = [None] * len(key_list)
        msg_tmp = msg_list[0:len(key_list)]

        for obj in range(len(key_list)):
            new_msg_tmp[key_list[obj][1]] = msg_tmp[obj]
        
        new_msg_list.extend(new_msg_tmp)
        msg_list = msg_list[len(key_list):]

    if (len(msg_list) > 0):
        backup_key_list = backup_key_list[0:len(msg_list)]
        backup_key_list.sort()

        new_msg_tmp = [None] * len(msg_list)

        for obj in range(len(backup_key_list)):
            new_msg_tmp[backup_key_list[obj][1]] = msg_list[obj]

        new_msg_list.extend(new_msg_tmp)

    #thing = np.array(new_msg_list)
    #print(str(thing.tobytes(), "utf-8"))
    return np.array(new_msg_list, dtype=np.uint8)




















