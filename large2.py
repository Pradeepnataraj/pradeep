l1=input().split()
n1=int(l1[1])
a=[int(k) for k in input().split()]
b1=sorted(a)
c1=b1[::-1]
print(c1[n1-1])
