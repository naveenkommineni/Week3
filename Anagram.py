#Anagrams
def Anagram(String1,String2):
    if sorted(String1)==sorted(String2):
        print("Two strings are anagrams")
    else:
        print("Strings are not anagrams")


Anagram('heat','eat')
    
    

