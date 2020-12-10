class Stack:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def pop(self):
        return self.items.pop()
    def push(self,data):
        self.items.append(data)
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return ''.join(map(str,self.items))
def computePostfix(input_str):
    it=Stack()
    for i in input_str:
        if i in '+-*/%':
            if i=='+':
                after=(it.pop())
                before=(it.pop())
                it.push(before+after)
            elif i=='*':
                after=(it.pop())
                before=(it.pop())
                it.push(before*after)
            elif i=='/':
                after=(it.pop())
                before=(it.pop())
                it.push(before/after)
            elif i=='-':
                after=(it.pop())
                before=(it.pop())
                it.push(before-after)
            elif i=='%':
                after=(it.pop())
                before=(it.pop())
                it.push(before%after)
        else:
            it.push(int(i))
    return print('result  -->  {}'.format(it))
def postfix_to_bracket_format(input_str):
    numstack = []
    for i in input_str:
        if i not in '+-*/%':
            numstack.append(i)
        else:   
            right = numstack.pop()
            left = numstack.pop() 
            newresult = ' '.join([left, i, right])
            bracket_format = '(' + newresult + ')'
            numstack.append(bracket_format)
    return print(numstack[0])
def postfix_to_infix(input_str):
    item=Stack()
    for i in input_str:
        if i in '+-*/%':
            if i =='+':
                after=item.pop()
                before=item.pop()
                item.push(before)
                item.push(i)
                item.push(after)
            elif i =='-':
                after=item.pop()
                before=item.pop()
                item.push(before)
                item.push(i)
                item.push(after)
            elif i =='*':
                after=item.pop()
                before=item.pop()
                item.push(before)
                item.push(i)
                item.push(after)
            elif i =='/':
                after=item.pop()
                before=item.pop()
                item.push(before)
                item.push(i)
                item.push(after)
            elif i =='%':
                after=item.pop()
                before=item.pop()
                item.push(before)
                item.push(i)
                item.push(after)
        else:
            item.push(int(i))
    return print('infix  --> {}'.format(item))

inp=input("Enter postfix : ").split()
computePostfix(inp)
postfix_to_bracket_format(inp)
postfix_to_infix(inp)


