class Queue:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def __str__(self):
        if  not self.isEmpty() :         
            return ''.join(self.items)

inp=input("Enter Input : ").split(',')
qEN=Queue()
qES=Queue()
for i in inp:
    if i.split()[0].startswith('EN'):
        qEN.enqueue(i.split()[1])
    elif i.split()[0].startswith('D'):
        if qES.isEmpty():
            if qEN.isEmpty():
                print("Empty")
            else:
                temp=qEN.dequeue()
                print(temp)
        else:
            temp=qES.dequeue()
            print(temp)
    else:
        qES.enqueue(i.split()[1])