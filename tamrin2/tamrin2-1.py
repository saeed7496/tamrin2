
time=input('inter time(hour:minute:seconds): ')
x=time.split(':')
result=int(x[0])*3600+int(x[1])*60+int(x[2])
print(result,'S')
