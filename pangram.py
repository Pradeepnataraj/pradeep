a=input()
a=a.lower()
a=a.replace(" ","")
b=set(a)
c=len(b)
if c==26:
    print("yes")
else:
    print("no")
