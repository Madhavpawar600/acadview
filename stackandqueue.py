print("enter the values in list seperated by space")

a=list(input().split())
def insertion(a):
    b=input("enter the element")
    a.append(b)
    return
def stackremove(a):
    a.pop()
    return

def queueremove(a):
    a.pop(0)
    return

          
print("use list as a queue press 1 or use list as stack press 2")
b=int(input())
c=True
if b==1:

    while c is True:
        print("to insert element in queue press 1 or to delete press 2 and to exit press any kess")
        d=int(input("enter your choice"))
        if d==1:
            insertion(a)
            print("after insertion")
            print(a)
        elif d==2:
            queueremove(a)
            print("after deletion")
            print(a)
        else:
            c=False
    
          

elif b==2:
    while c is True:
        print("to insert element in stack press 1 or to delete press 2 and to exit press any kess")
        d=int(input("enter your choice"))
        if d==1:
            insertion(a)
            print("after insertion")
            print(a)
        elif d==2:
            stackremove(a)
            print("after deletion")
            print(a)
        else:
            c=False
        

else:
    pass

