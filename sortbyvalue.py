dic1={'n':'tarun','t':'likhith','s':'santosh'}
for i in sorted(dic1.values()):
    for j in dic1.keys():
        if dic1[j]==i:
            print(j,i)

