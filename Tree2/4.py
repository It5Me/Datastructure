def sumall(k):
    summ=0
    for x in k:
        summ+=x
    return summ
def com(n):
    if n>=len(keeppower):
        return 0
    else:
        keeppower[n]=com(2*n+1)+com(2*n+2)+keeppower[n]
        return keeppower[n]
inp,compare=input('Enter Input : ').split('/')
keeppower=[]
for i in inp.split():
    keeppower.append(int(i))
print(com(0))
for j in compare.split(','):
    front=keeppower[int(j.split()[0])]
    behind=keeppower[int(j.split()[1])]
    if front>behind:
        print('{}>{}'.format(j.split()[0],j.split()[1]))
    elif front<behind:
        print('{}<{}'.format(j.split()[0],j.split()[1]))
    else:
        print('{}={}'.format(j.split()[0],j.split()[1]))



    




