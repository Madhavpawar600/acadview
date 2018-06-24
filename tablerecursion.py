def table(n,a=1):
    if a==11:
        return
    print(n*a)
    return table(n,a+1)
n=int(input())
table(n)
