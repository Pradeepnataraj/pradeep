x1,y1=input().split();
x2,y2=input().split();
x3,y3=input().split();
x4,y4=input().split();
if(x1==x2 and x3==x4 or x1==x3 and x2==x4):
    if(y1==y2 and y3==y4 or y1==y3 and y2==y4):
        print("true");
    else:
        print("false");
else:
    print("false");
