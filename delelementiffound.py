n=list(map(int,input().split()))
a=int(input())
flag=0
for i in n:
    if i==a:
        n.remove(i)
        print("successfully delete the element",a)
        flag=1

if flag==1:
    print(n)
else:
    print("element not found")


