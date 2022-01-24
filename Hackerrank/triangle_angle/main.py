# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, acos, cos, degrees, radians, atan
BC=int(input("a: "))    # a Adjacent side
AB=int(input("b: "))    # c Opposite side
AC=sqrt(AB**2+BC**2)    # b Hypotenuse
MC=AC/2                 # Length of MC same as AM
# Solve using law of sines 
angC = degrees(acos((AB**2-BC**2-AC**2)/(-2*BC*AC)))
angA = degrees(acos((BC**2-AB**2-AC**2)/(-2*AB*AC)))
theta = 180-(90+angC)
# 2 methods of solving the problem
print(f"{round(theta)}\N{DEGREE SIGN}")
print(f"{180-(round(degrees(atan(AB/BC)))+90)}\N{DEGREE SIGN}")


# a^2 = b^2+c^2-2*b*c*cos(A)
# b^2 = a^2+c^2-2*a*c*cos(B)
# c^2 = a^2+b^2-2*a*b*cos(C)

# cos(A) = (a^2-b^2-c^2)/(-2bc)
# cos(B) = (b^2-a^2-c^2)/(-2ac)
# cos(C) = (c^2-a^2-b^2)/(-2ab)
