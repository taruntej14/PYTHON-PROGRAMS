a=[]
b=[]
while True:
    n=int(input("enter a number"))
    if n==0:
         break
    else:
        a.append(n)
print("min is ",min(a))
print("max is",max(a))
print("range is",max(a)-min(a))
n1=sum(a)/len(a)
n2=0.0
for i in a:
    n2=(n2+(i-n1)**2)/len(a)-1
print("variance is",n2)
b=sorted(a)
if len(a)%2!=0:
    print("median is",b[len(b)//2])
else:
    print("median is",(b[len(b)//2]+b[len(b)//2-1])/2)

