# pradeep
str1 = input()
a=['a','e','i','o','u','A','E','I','O','U']
for j in range(0,len(str1)):
    for i in range(0,10):
        if str1[j] in a[i]:
            b=a
            print(b[i],end="")
str1= str1.replace('a',"")
str1= str1.replace('e', "")
str1= str1.replace('i', "")
str1= str1.replace('o', "")
str1= str1.replace('u', "")
str1= str1.replace('A',"")
str1= str1.replace('E', "")
str1= str1.replace('I', "")
str1= str1.replace('O', "")
str1= str1.replace('U', "")
print(str1)
