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
        return str(' '.join(self.queue))

data,q=input("Enter Input : ").split('/')
data=data.split(',')
q=q.split(',')
item=Queue()
li=[]
team=[]
for x in q:
    if x=='D':
        print(item)
    elif x.startswith('E'):
        item.enqueue(x.split()[1])
        li.append()