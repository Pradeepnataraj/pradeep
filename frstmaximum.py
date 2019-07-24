# pradeep
n = int(input())
arr = []
a=input().split()
b=n/2
b=int(b)
for i in range(0,n):
    arr.append(int(a[i]))
for i in range(0,b):
    print(max(arr),min(arr),end=" ")
    arr.remove(max(arr))
    arr.remove(min(arr))
if(n%2!=0):
    print(min(arr),end=" ")
