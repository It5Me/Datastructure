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
        return str(self.queue)    

inp=input("Enter Input : ").split(",")
it=Queue()
count=0
for i in inp:
    if i.split()[0]=='E':
        it.enqueue(i.split()[1])
        print("Add {} index is {}".format(i.split()[1],count))
        count+=1
    else:
        if it.size()<=0:
            print("-1")
        elif it.size()>0:
            y=it.dequeue()
            size=it.size()
            print("Pop {} size in queue is {}".format(y,size))
            count-=1
else:
    if it.size()>0:
        print("Number in Queue is :  {}".format(it))
    else:
        print("Empty")                