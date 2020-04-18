import math
import sys
def Windchill():
    t=float(sys.argv[1])
    v=float(sys.argv[2])
    if t>50 and v>120 or v<3:
        print("Formulea is not valid")
    else:
        a=pow(v,0.16)
        w=(35.74+0.62158*t+(0.4275*t-35.75)*a)
        print ("Effective temperature is:",w)
Windchill()
                
