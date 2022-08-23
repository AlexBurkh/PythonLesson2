# Реализуйте алгоритм перемешивания списка.

from time import time

def random(length):
    seed = time()
    result = int(seed**2/pow(10,(length/2))) % length
    return result
    


def rotate_list(list_to_rotate):
    out_list = list_to_rotate
    for index in range(len(list_to_rotate)):
        pos = random(len(list_to_rotate)) % len(list_to_rotate)
        out_list[index], out_list[pos] = out_list[pos], out_list[index]
    return out_list



in_list = [0, 1, 2, 3, 4]
print(in_list)
print(rotate_list(in_list))

