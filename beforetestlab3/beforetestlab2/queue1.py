class Queue:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def enQueue(self,data):
        self.items.append(data)
    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return -1
    def __str__(self):
        if  not self.isEmpty():
            return str(self.items)
        else:
            return str('Empty')

inp=input("Enter Input : ").split(',')
q=Queue()
for i in inp:
    if i.split()[0].startswith('E'):
        q.enQueue(i.split()[1])
        print('Add {} index is {}'.format(i.split()[1],q.size()-1))
    else:
        temp=q.deQueue()
        if int(temp)>=0:
            print("Pop {} size in queue is {}".format(temp,q.size()))
        else:
            print(temp)
print(q)

    