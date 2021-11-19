def list_xor(n, list1, list2):
    return n in list1 and n not in list2 or n in list2 and n not in list1 

print(list_xor(1, [0, 2, 3], [1, 5, 6]))