#Insertion sort
L=[2,8,22,13,16,5,41,10]
def Insertion_sort(L):
    for index in range(1,len(L)): #Starts from 1 as 0th index is taken as sorted
        current_element=L[index]
        pos=index
        while current_element<L[pos-1] and pos>0:
            L[pos]=L[pos-1]
            pos=pos-1
        L[pos]=current_element

Insertion_sort(L)
print("Sorted list is:",L)
