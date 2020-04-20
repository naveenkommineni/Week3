import sys
n=int(sys.argv[1])
for i in range(n+1):
    a=2**i
    if a<=2**n:
           print("2**",i,":",a)
            
