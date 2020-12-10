def hanoi(n,start,end,buff):
    if n == 0:
        return
    hanoi(n-1,start,buff,end)
    print(start,'To',end)
    hanoi(n-1,buff,end,start)
hanoi(4,'A','C','B')

