n=int(input('Enter the number:'))
i=2
pf=[]
while i*i<=n:
    while n>1:
        while n%i==0:
            pf.append(i)
            n=n/i
        i+=1
print(pf)
