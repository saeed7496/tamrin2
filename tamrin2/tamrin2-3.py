# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 00:05:09 2022

@author: saeed
"""
result=[]
tedad=int(input('pleaz inter number of studends: '))
for i in range(tedad):
    sume=float(input(f'pleaz add scor{i+1}: '))
    if 20>= sume>=0:
        result.append(sume)
    else:
        result='namotabar'
print('\nsum scors is: ',sum(result))
print('max scors is: ',max(result))
print('min scors is: ',min(result))
print('avrage scors is: ',round((sum(result)/len(result)),2))


