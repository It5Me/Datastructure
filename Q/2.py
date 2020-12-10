class Queue:
    def __init__(self,li=None):
        if li==None:
            self.queue=[]
        else:
            self.queue=li
    def enqueue(self,items):
        self.queue.append(items)
    def dequeue(self):
        if len(self.queue)<1:
            return None
        else:
            return self.queue.pop(0)
    def size(self):
        return len(self.queue)
    def __str__(self):
        return str(''.join(self.queue))

inp=input("Enter Input : ").split(",")
itemES=Queue()
itemEN=Queue()
st=False
for i in inp:
    if i.split()[0]=='D':
        # print("size ES",itemES.size())
        # print("size EN",itemEN.size())
        if itemEN.size()==0  and itemES.size()==0 and st==False:
            print("Empty")
        elif itemES.size()>0:
            e=itemES.dequeue()
            print(e)
               
        elif itemES.size()<=0 and itemEN.size()>0:
            t=itemEN.dequeue()
            print(t) 
            
               
    elif i.split()[0]=='EN':
        itemEN.enqueue(i.split()[1])
        # print(i.split()[1])
    else:
        itemES.enqueue(i.split()[1])
        # print(i.split()[1])
