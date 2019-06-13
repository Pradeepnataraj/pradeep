import math
x,y=[int(x) for x in input().split()]
a,b=[int(a) for a in input().split()]
c=math.fabs(x-a)
d=math.fabs(y-b)
c=int(c)
d=int(d)
print(c,d)
