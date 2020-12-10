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
        if  not self.isEmpty():         
            return ''.join(self.items)
def encodemsg(string,num):
    tempstring=Queue(list(''.join(string.items).replace(' ','')))
    tempnum=Queue(num.items.copy())
    li=[]
    for i in range(string.size()): 
        temp=string.dequeue()
        if 'A'<=temp<='Z' or 'a'<=temp<='z':
            tempn=tempnum.dequeue()
            if  'a'<=chr((ord(temp)+int(tempn)))<='z' or 'A'<=chr((ord(temp)+int(tempn)))<='Z':
                li.append(chr(ord(temp)+int(tempn)))
                # print('do1')
                tempnum.enqueue(tempn)
            elif chr((ord(temp)+int(tempn)))>'z':
                # print('do2')
                s=chr((ord(temp)+int(tempn))-ord('z')+ord('a')-1)
                # print('chr',(ord(temp)+int(tempn))-ord('z'))
                li.append(s)
                tempnum.enqueue(tempn)
            elif chr((ord(temp)+int(tempn)))>'Z':
                # print('do3')
                s=chr((ord(temp)+int(tempn))-ord('Z')+ord('A')-1)
                li.append(s)
                tempnum.enqueue(tempn)
    for i in li:
        string.enqueue(i)
    return print(string)

def decodemsg(string,num):
    print("string",string.items)
    # print(num)
    tempstring=Queue(list(string.items.copy()))
    print(Queue(list(string.items)))
    print(tempstring.items)
    tempnum=Queue(num.items.copy())
    li=[]
    for i in range(string.size()): 
        temp=tempstring.dequeue()
        if 'A'<=temp<='Z' or 'a'<=temp<='z':
            tempn=tempnum.dequeue()
            if 'a'<=chr((ord(temp)-int(tempn)))<='z' or 'A'<=chr((ord(temp)-int(tempn)))<='Z':
                print('do1',temp)
                li.append(chr(ord(temp)-int(tempn)))
                tempnum.enqueue(tempn)
            elif chr((ord(temp)-int(tempn)))<'A':
                print('do3',temp)
                s=chr(ord('Z')-(ord(temp)-ord('A')+int(tempn))+1)
                print('n2',ord('Z')-(ord(temp)-ord('A')+int(tempn))+1)
                li.append(s)
                tempnum.enqueue(tempn)
            elif chr((ord(temp)-int(tempn)))<'a':
                print('do2',temp)
                s=chr(ord('z')-(ord(temp)-ord('a')+int(tempn))+1)
                print('n',chr(ord('z')-(ord(temp)-ord('a')+int(tempn))+1),tempn)
                li.append(s)
                tempnum.enqueue(tempn)
            
    for i in li:
        string.enqueue(i)
    return print(li)


    
string,number=input("Enter String and Code : ").split(',')
q1 = Queue(list(string))
q2 = Queue(list(number))
encodemsg(q1, q2)
decodemsg(q1, q2)