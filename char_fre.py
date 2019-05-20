dt={}
s=input("enter a string")
for c in s:
    dt.update({c:s.count(c)})
for i,j in dt.items():
    print(i,j)
