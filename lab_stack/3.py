class Stack:
    def __init__(self,n=None):
        if n is None:
            self.li=[]
        else:
            self.li=n
    def push(self,v):
        self.li.append(v)
    def peek(self):
        return self.li[-1]
    def pop(self):
        return self.li.pop()
    def size(self):
        return len(self.li)
    def is_empty(self):
        return len(self.li)==0
    def __str__(self):
        return ''.join(self.li[::-1])   

inp=input("Enter Input : ").split(" ")
#inp="C C C A A A".split(" ")[::-1]
#print(inp)
stack=Stack()
count=0
combo=0
maxcombo=0
for x in inp:
    if not('A'<=x<='Z'):
        continue
    if stack.is_empty():
       stack.push(x)
       count=1 
    else:
        if stack.peek()==x:
            count+=1
            if count==3:
                #print("pop"+stack.pop())
                #print("pop"+stack.pop())
                stack.pop()
                stack.pop()
                if stack.size()>=2:
                    temp=stack.pop()
                    if temp==stack.peek():
                        count=2
                    else:
                        count=1
                    stack.push(temp)
                elif stack.size()==1:
                    count=1
                else:
                    count=0        
                combo+=1     
            else:
                stack.push(x)
                #print("push"+x)    
        else:
            #maxcombo=max(maxcombo,combo)
            #combo=0
            count=1
            stack.push(x)
            # print("push"+x)
        #print("count",count)
#combo=max(maxcombo,combo)     
print(stack.size())
if stack.size()==0:
    print("Empty")
else:
    print(stack)    
if combo>1:
    print("Combo : {} ! ! !".format(combo))

                    


