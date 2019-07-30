# pradeep
s,p=input().split()
a=len(p)
for i in range(len(s)):
    b=s[:a]
    d=len(s)
    s=s[-(d-1):]
    if(p==b):
        print("yes")
        break
else:
    print("no")
