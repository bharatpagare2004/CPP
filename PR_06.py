s=input("enter a main string:")
while(1):
    print("\n1.length\2.reverse\n3.equality of two string\n4.cheak palindrom\n5.cheak substring\n6.exit\n")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("length of string",len(s))
    elif choice==2:
        print("reverse string is",s[::-1])
    elif choice==3:
        s1=input("enter astring to compare:")
        if s==s1:
            print("equal")
        else:
            print("not equal")
    elif choice==4:
        if s==s[::-1]:
            print("palindrome")
        else:
            print("not palindrome")
    elif choice==5:
        s2=input("enter substring to cheak:")
        if s2 in s:
            print("substring is present")
        else:
            print("substring is not present")
    elif choice==6:
        break  
    else:
        print("invalide choice")                                          