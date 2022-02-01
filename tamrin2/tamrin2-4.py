
import random
while True:
    start=input('inter S or c: ').upper()
    if start =='S':
        while True:
            tas=random.randint(1, 6)
            print(tas)
            if tas == 6:
                continue
            else:break
    elif start == 'C':
        break
    else:
        print('wrong!!pleaz choose s or c')
        continue
print('End')       
            
            
            
            
            
