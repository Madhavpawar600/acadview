a="mississippi"
a=list(a)
b=set(a)
b=list(b)
dict1={}
for i in range(0,len(b)):
    count=0
    for j in range(0,len(a)):
        if b[i]==a[j]:
            count+=1
        dict1.update({b[i]:count})
print(dict1)
