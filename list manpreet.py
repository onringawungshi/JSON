a=[[1,2,3],[4,5,1],[6,7,1]]
i=0
s=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==0:
            s=s+a[i][j]
        else:
            s=s+a[i][-1]
            break
        j+=1
    i+=1
print(s)
