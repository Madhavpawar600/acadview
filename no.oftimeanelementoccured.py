a=list(input().split())
b=set(a)
b=list(b)
for i in range(0,len(b)):
    count=0
    for j in range(0,len(a)):
       if b[i]==a[j]:
           
           count+=1
    print(b[i],"=",count)
