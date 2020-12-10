class Stack:
    def __init__(self,l=None):
        if l==None:
            self.items=[]
        else:
            self.items=l
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if self.size()==0:
            return ''
        else:
            return self.items.pop()
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return str(self.items)
class StackCalc:
    def __init__(self):
        self.stack=Stack()
    def run(self,ar):
        for i in ar.split():
            if '0'<=i<='9':
                self.stack.push(int(i))
            elif i =='+':
                f=self.stack.pop()
                b=self.stack.pop()
                self.stack.push(int(f+b))
            elif i =='-':
                f=self.stack.pop()
                b=self.stack.pop()
                self.stack.push(int(f-b))
            elif i =='*':
                f=self.stack.pop()
                b=self.stack.pop()
                self.stack.push(int(f*b))
            elif i =='/':
                f=self.stack.pop()
                b=self.stack.pop()
                self.stack.push(int(f/b))
            elif i =='DUP':
                self.stack.push(self.stack.peek())   
            elif i=='POP':
                if self.stack.size==0:
                    return 0
                else:
                    self.stack.pop()
            else:
                while self.stack.size()!=0:
                    self.stack.pop()
                self.stack.push("Invalid instruction: {}".format(i))
                break
                    
    def getValue(self):
        if self.stack.size()==0:
            return 0
        else:
            return self.stack.peek()
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue()) 