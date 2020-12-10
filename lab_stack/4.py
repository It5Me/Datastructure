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
        if self.size==0:
            return ''
        else:
            return self.li.pop()
    def size(self):
        return len(self.li)
    def is_empty(self):
        return len(self.li)==0
    def __str__(self):
        return ''.join(self.li)

class StackCalc:
    def __init__(self):
        self.stack=Stack()
    def run(self,arg):
        for x in arg.split():
            if '0'<=x<='9':
                self.stack.push(int(x))
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
            elif x=="POP":
                self.stack.pop()
            else:
                while self.stack.size()!=0:
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