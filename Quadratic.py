def Quadratic():
    a=int(input('enter value of a:'))
    b=int(input('enter value of b:'))
    c=int(input('enter value of c:'))
    s=((b*b)-(4*a*c))
    e=(s)**(1/2)
    Root1=((-b+e)/(2*a))
    Root2=((-b-e)/(2*a))
    print('Root1 of X:',Root1)
    print('Root2 of X:',Root2)
Quadratic()
