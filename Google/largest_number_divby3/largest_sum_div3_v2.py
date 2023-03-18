def solution(l):
    one, two = [], []
    l_sum = sum(l)

    for num in l:
        if num % 3 == 1:
            one.append(num)
        elif num % 3 == 2:
            two.append(num)
    
    one.sort()
    two.sort()
    
    if l_sum % 3 == 0:
        l.sort(reverse=True)
        return int(''.join(map(str, l)))
    elif l_sum % 3 == 1:
        if len(one) >= 1:
            l.remove(one[0])
        else:
            l.remove(two[0])
            l.remove(two[1])
    else:
        if len(two) >= 1:
            l.remove(two[0])
        else:
            l.remove(one[0])
            l.remove(one[1])
    l.sort(reverse=True)
    return int(''.join(map(str, l)))
