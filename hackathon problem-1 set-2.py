def isPalindrome(s):
    if(s==s[::-1]):
        print(1)
    else:
        print(0)

s=input("enter the string:")
isPalindrome(s)