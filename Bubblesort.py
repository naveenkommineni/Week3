#Bubble Sort
L=[2,8,22,31,14,11]
def Bsort(L):
    for index in range(len(L)-1,0,-1): #Loop from last to first element
        for next in range(index):
            if L[next]>L[next+1]:
                L[next],L[next+1]=L[next+1],L[next]  #swapping of elements in list
Bsort(L)
print("Sorted list is:",L)
