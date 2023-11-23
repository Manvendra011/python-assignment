# function which returns reverse of a string
def isPalindindrome(s):
    return s==s[::-1]


#Driver code
s = "naman"
ans = isPalindindrome(s)

if ans :
    print("yes")
else:
    print ("no")    