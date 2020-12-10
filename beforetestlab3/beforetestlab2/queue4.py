class Queue:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def __str__(self):
        return ' '.join(self.items)
    def insert(self,index,data):
        self.items.insert(index,data)

inp=input("Enter Input : ").split('/')
id_people=Queue()
num_people=Queue()
left=inp[0]
rigth=inp[1]
qe=Queue()
numq=Queue()
print(left)
for i in rigth.split(','):
    if i.startswith('D'):
        print(qe.dequeue())
        numq.dequeue()
    elif i.startswith('E'):
        idpe=i.split()[1]
        for x in left.split(','):
            if idpe==x.split()[1]:
                if x.split()[0] in numq.items:
                    inde=numq.items.index(x.split()[0])
                    count=0
                    for j in range(inde,numq.size()):
                        if numq.items[j]!=x.split()[0]:
                            break
                        count+=1
                    numq.insert( (inde+count),x.split()[0])
                    qe.insert((inde+count),x.split()[1])
                else:
                    numq.enqueue(x.split()[0])
                    qe.enqueue(i.split()[1])

            
# print(qe.items)
# print(numq)


    