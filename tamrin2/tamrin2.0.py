
sum=0
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
while True:
    number=input('add number: ')
    if isfloat(number)==True:
        number=float(number)
        sum+=number
    elif number=='exit':
        break
    else:
        print('Error!! number is false')
print(sum)








