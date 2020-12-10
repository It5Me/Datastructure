class Stack:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def pop(self):
        return self.items.pop()
    def push(self,data):
        self.items.append(data)
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def __str__(self):
        return ''.join(self.items[::-1])
inp=input("Enter Input : ").split()
it=Stack()
count=0
combo=0
tempcom=0
combo_max=-1
for i in inp:
    if it.isEmpty():
        it.push(i)
        count+=1
    else:
        if it.peek()==i:
            count+=1
            it.push(i)
            if count==3:
                it.pop()
                it.pop()
                it.pop()
                count=0
                combo+=1
                if it.size()<=1:
                    count=it.size()
                else:
                    temp=it.pop()
                    if temp==it.peek():
                        count=2
                        it.push(temp)
                    else:
                        count=1
                        it.push(temp)
                
        else:
            it.push(i)
            count=1
            if combo>combo_max:
                    combo_max=combo
            else:
                combo=0
if it.size()==0:
    print('Empty')
else:
    print(it)
print('combo',combo)
