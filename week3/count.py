a=input("enter the sentences:")
words=a.lower().split()
b={}
for i in words:
    b[i]=b.get(i,0)+1
    print(b)

