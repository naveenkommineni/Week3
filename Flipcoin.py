#Flip coin prob
lst=['H','T']
import random
heads=0
tails=0
for i in range(22):
    n=random.choice(lst)
    if n=='H':
        heads+=1
    else:
        tails+=1
print('Number of heads:',heads)
print('Number of tails:',tails)
poh=(heads/i)*100
pot=(tails/i)*100
print('probability percentage of heads:',poh)
print('probability percentage of tails:',pot)
