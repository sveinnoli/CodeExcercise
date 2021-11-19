def consecutive_zeros(binary):
    return max([len(s) for s in binary.split("1")])

print(consecutive_zeros("1001101000110"))