#Temp conversion
def Conversion():
    sel=input("enter selection:")
    if sel=="FtoC":
        F=float(input('Enter the temperature to convert:'))
        C=(F-32)*(5/9)
        print('Temperature in celsius:',C)
    elif sel=="CtoF":
        C=float(input('Enter the temperature to convert:'))
        F=C*1.8+32
        print('Temperature in farehiet is:',F)
    else:
        print("Selection invalid")

Conversion()
        
