def findmax(st):
    if len(st)==1:
        return st[0]
    temp = findmax(st[:-1])
    if st[-1]> temp:
        return st[-1]  
    else:
        return temp

print(findmax([10,2,3,4,5,6,7,8,9]))
# print('123'[:-1])