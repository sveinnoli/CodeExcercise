# Program that converts N into a numerical triangle of height N-1 so 5 becomes: 1, 22, 333, 4444
from functools import reduce
for i in range(1,int(input())): 
    # print( int(((10**i//10)) * (i*10/9)))
    # print((10**(i)//9)*i)
    print(reduce(lambda x,y: x*10+y, [i]*i))