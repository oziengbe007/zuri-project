
def tellAnagram():
    while True:
        a=input("\nEnter string 1:")
        
        b=input("Enter string 2:")
        
        acount = 0
        aLen = len(a)
        bLen = len(b)
        if aLen != bLen:
            print("Not an Anagram")
            break
        for i in range(aLen):
            v = a[i]
            if v in b:
                acount = acount +1
        print (f"\n{acount} found, {aLen} needed\n")
        if acount != aLen:
            print("Words are not Anagrams")
        else:
            print("Words are anagrams")
tellAnagram()

