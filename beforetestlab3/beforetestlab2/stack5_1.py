class Stack:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def isEmpty(self):
        return  self.items==[]
    def size(self):
        return len(self.items)
    def pop(self):
        return self.items.pop()
    def push(self,data):
        self.items.append(data)
    def peek(self):
        return self.items[-1]
    def __str__(self):
        if not self.isEmpty():
            return ''.join(str(self.items))
        else:
            return 'Empty'
    def clear(self):
            self.items=[]
inp=input("Enter Input : ").split(',')
it=Stack()
itS=Stack()
m=-1
n=-1
eat=False
item=Stack()
for i in inp:
    if i.split()[0]=='A':
            item.push(i.split()[1])
            if int(i.split()[1])>m:
                for j in range(it.size()):
                    it.pop()
                it.push(i.split()[1])
                m=int(i.split()[1])
            else:
                if it.isEmpty():
                    it.push(int(i.split()[1]))
                    m=int(i.split()[1])
                elif not it.isEmpty() and int(i.split()[1]) < int(it.peek()) and int(i.split()[1])!=it.peek() :
                    it.push(int(i.split()[1]))           
    elif i.split()[0]=='B':
        if eat==False:
            print(it.size())
        else:
            for i in item.items:
                temp=int(i)
                if temp%2==0:
                    temp=temp-1
                    print(temp)
                    if  not itS.isEmpty() and temp>n:
                        for i in range(itS.size()):
                            itS.pop()
                        itS.push(temp)
                        n=temp
                    else:
                        if itS.isEmpty():
                            itS.push(temp)
                            n=temp
                            print('n',n)
                        elif not itS.isEmpty() and temp<itS.peek() and temp!=itS.peek():
                            itS.push(temp)
                    print(itS)
                else:
                    temp=temp+2
                    if not itS.isEmpty() and temp>n:
                        for i in range(itS.size()):
                            itS.pop()
                        itS.push(temp)
                        n=temp
                    else:
                        if itS.isEmpty():
                            itS.push(temp)
                            n=temp
                        elif  not itS.isEmpty() and temp<int(itS.peek()) and temp!=itS.peek():
                            itS.push(temp)
                    print(itS)
            print(item.items)
            print(itS.items)
            print(itS.size())
            eat=False
            itS.clear()                  
    else:
        eat=True

        
