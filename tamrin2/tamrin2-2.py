
seconds=int(input('inter seconds: '))
hour=divmod(seconds,3600)
minute=divmod(hour[1],60)
second=minute[1]
print(hour[0],minute[0],second,sep=':')