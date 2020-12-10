class Stack:
    def __init__(self,n=None):
        if n==None:
            self.li=[]
        else:
            self.li=n
    def is_empty(self):
        return len(self.li)==0
    def size(self):
        return len(self.li)
    def pop(self):
        return self.li.pop()
    def push(self,v):
        self.li.append(v)
    def peek(self):
        return self.li[-1]            
    def __str__(self):
        return str(self.li)
class StackCalc:
    def __init__(self):
        self.stack=Stack()        
    def run(self,arg):
        for x in arg.split():
            if '0'<=x<='9':
                self.stack.push(int(x))
                print(self.stack)   
            elif x=='+':
                self.stack.push(self.stack.pop()+self.stack.pop())
            elif x=='-':
                self.stack.push(self.stack.pop()-self.stack.pop())
            elif x=='*':
                self.stack.push(self.stack.pop()*self.stack.pop())
            elif x=='/':
                self.stack.push(int(self.stack.pop()/self.stack.pop()))           
            elif x=='DUP':
                 self.stack.push(self.stack.peek())
            elif x=='POP':
                self.stack.pop()
            elif x=='PSH':
                self.stack.push(x)
            else:
                while self.stack.size()!=0:
                    print("while")
                    self.stack.pop()
                self.stack.push("Invalid instruction: {}".format(x))
                break    
    def getValue(self):
        return str(self.stack.peek()) if self.stack.size()>0 else 0              

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())                    