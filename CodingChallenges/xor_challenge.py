def list_xor(n, list1, list2):
    if n in list1:
        return n not in list2
    elif n in list2:
        return True
    return False
    #return n in list1 and n not in list2 or n in list2 and n not in list1 


print(list_xor(1, [1, 2, 3], [0, 5, 6]))