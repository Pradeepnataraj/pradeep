from itertools import combinations
a,b=map(int,input().split())
c=len(str(a))
lst1=list(combinations(str(a),c-b))
lst1=sorted(lst1)
print(*lst1[0],sep='')
