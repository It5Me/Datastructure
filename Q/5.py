class Queue:
    def __init__(self, li=None):
        if li == None:
            self.queue = []
        else:
            self.queue = li

    def enqueue(self, items):
        self.queue.append(items)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)
    def pop(self):
        return self.queue.pop()         
    def size(self):
        return len(self.queue)
    def __str__(self):
        return str(', '.join(self.queue))
    def front(self,i):
        self.queue.insert(0,i)

nor,mir=input("Enter Input (Normal, Mirror) : ").split()
item=Queue()
itnor=Queue()
count=0
count1=0
tempp=""
temp=""
countBoommir=0
li=[]
li2=[]
for x in list(reversed(mir)):
    if item.size()==0:
        item.enqueue(x)
        temp=x
        count+=1
        # print("first {} f {}".format(x,count))
    else:
        if temp==x:
            count+=1
            item.enqueue(x)
            # print("{} on {}".format(x,count))
            if count==3:
                li.append(x)
                # print("boom",x)
                item.pop()
                item.pop()
                item.pop() 
                count=0
                countBoommir+=1
                if item.size()==1:
                    te=item.dequeue()
                    item.front(te)
                    count+=1
                    temp=te
                    # print("item ",item)
                    # print("under",count)
                elif item.size()>=2:
                    temp1=item.dequeue()
                    temp2=item.dequeue()
                    item.front(temp2)
                    item.front(temp1)
                    temp=temp1
                    if temp1==temp2:
                        count=2 
                    else:
                        count=1                      
        else:
            item.enqueue(x)
            temp=x
            count=1
count_nor=0
failed=0                     
for x in nor:
    if itnor.size()==0:
        itnor.enqueue(x)
        tempp=x
        count1+=1
        # print("first {} f {}".format(x,count))
    else:
        if tempp==x:
            count1+=1
            itnor.enqueue(x)
            # print("{} on {}".format(x,count))
            if count1==3:
                if len(li)>0:
                    pim=itnor.pop()
                    if li[0]==pim:
                        itnor.pop()
                        itnor.pop()
                        count1=1
                        failed+=1
                        itnor.enqueue(li[0])
                        li.pop(0)
                    else:    
                        itnor.enqueue(li[0])
                        li.pop(0)
                        itnor.enqueue(pim)
                        count1=1
                else:
                    itnor.pop()
                    itnor.pop()
                    itnor.pop()
                    count_nor+=1  
                # print("boom",x)
                    count1 = 0
                    if itnor.size()==1:
                        te=itnor.queue[-1] 
                        # itnor.front(te)
                        count1=1
                        tempp=te
                        # print("item ",item)
                        # print("under",count)
                    elif itnor.size()>=2:
                        temp1=itnor.queue[-2]
                        temp2=itnor.queue[-1]
                        # itnor.front(temp2)
                        # itnor.front(temp1)
                        tempp=temp1
                        if temp1==temp2:
                            count1=2
                        else:
                            count1=1                      
        else:
            itnor.enqueue(x)
            tempp=x
            count1=1
st=''.join(itnor.queue)
print("NORMAL :")
print(itnor.size())
if itnor.size() != 0:
    print(st[::-1])  
else:
    print('Empty') 
print(f'{count_nor} Explosive(s) ! ! ! (NORMAL)')
if failed != 0:
    print(f'Failed Interrupted {failed} Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(item.size())
if item.size() != 0:
    print(''.join(list(reversed(item.queue))))
else:
    print('ytpmE')
print(f'(RORRIM) ! ! ! (s)evisolpxE {countBoommir}')



            


    



        
        
     
