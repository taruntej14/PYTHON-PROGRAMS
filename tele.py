dic1={}
while True:
    name=input("enter your name")
    if name=='end':
        break
    num=int(input("enter your phone number"))
    dic1.update({name:num})
print(dic1)
