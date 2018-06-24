def power(b,e):
    if(e==1):
        return(b)
    if(e!=1):
        return(b*power(b,e-1))

b=int(input("enter  base"))
e=int(input("enter exponential value:"))
print("result:",power(b,e))
