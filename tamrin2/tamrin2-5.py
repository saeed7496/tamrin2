
f=[0,1]
n=int(input('inter number: '))
for i in range(2, n):
    f.append(f[i-1]+f[i-2])
for j in f:
    print(j,sep='...',end=' ')

















