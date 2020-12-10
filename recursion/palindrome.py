def palindrome(inp):
    if len(inp)==0:
        return True
    if inp[0]==inp[-1]:
        inp = inp[1:-1:1]
        return palindrome(inp)
    else:
        return False
    
inp=input("Enter Input : ")
if palindrome(inp):
    print("'{}' is palindrome".format(inp))
else:
    print("'{}' is not palindrome".format(inp))