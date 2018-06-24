ls=[1,2,3,"madhav",9.99,"str",0.98]
dict1={}

for i in range(0,len(ls)):
    dict1.update({ls[i]:type(ls[i])})

print(dict1)
                 
