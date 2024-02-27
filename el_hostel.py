'''
Código fuente de https://www.youtube.com/watch?v=n2uGW4nmLRE

'''

import random

l1 = ['AL1', '10L1', '11L1', '12L1']
l2 = ['AL2', '10L2', '11L2', '12L2']
l3 = ['AL3', '10L3', '11L3', '12L3']
l4 = ['AL4', '10L4', '11L4', '12L4']

lt = l1 + l2 + l3 + l4


for a in (0,random.randint(0, 9)):
    for i in range (0,random.randint(0, 9)):
        temp = lt[0] # tengo la primera carta
        for j in range(0,16):
            try:
                lt[j] = lt[j+1]
            except:
                pass
        lt[len(lt)-1] = temp

l1 = []
l2 = []
l3 = []
l4 = []
    
for i in range(0, len(lt)):
    t = i % 4
    if t == 0:
        l1.append(lt[i])
    elif t == 1:
        l2.append(lt[i])
    elif t == 2 :
        l3.append(lt[i])
    else:
        l4.append(lt[i])
print(l1)
print(l2)
print(l3)
print(l4)
