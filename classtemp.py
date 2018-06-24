class temperature:
    
    def celcius(self,deg):
       s=(deg-32)*5/9
       print(s,"c")


    def farhnite(self,deg):
        f=(deg*1.8)+32
        print(f,"f")


print("press 1 for convert celsius to fahrenheit and press 2 for convert fahernheit to celcius")
n=int(input())
c1=temperature()
if n==1:
    a=int(input("enter the celsius value"))
    c1.farhnite(a)

elif n==2:
    a=int(input("enter the fahrenheit value"))
    c1.celcius(a)    
