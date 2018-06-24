try:
    a=3
    if a<4:
        b=a//a-3
        if(a-3==0):
            raise Execption()
except Exception:
    print("division by zero error")
else:
    print("success")
