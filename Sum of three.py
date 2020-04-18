def Sumofthree():
    l=int(input("Enter the legth of array:"))
    a=[]
    for elements in range(l):
        el=int(input("enter element:"))
        a.append(el)
    for start in range(0,l-2):
        for next in range(start+1,l-1):
            for end in range(next+1,l):
                if (a[start]+a[next]+a[end]==0):
                    print("Triplets are:",a[start],a[next],a[end])
Sumofthree()
                    
