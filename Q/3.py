class Queue:
    def __init__(self,li=None):
        if li==None:
            self.queue=[]
        else:
            self.queue=list(li)
    def enqueue(self,items):
        self.queue.append(items)
    def dequeue(self):
        if len(self.queue)<1:
            return None
        else:
            return self.queue.pop(0)
    def size(self):
        return len(self.queue)
def encodemsg(s,n):
    li=[]
    temp=n.queue
    ind_let=0
    ind_n=0
    letter=''.join(s.queue).replace(' ','') 
    #i zove Python,256183
    while ind_let<len(letter):
        if ord('a')<=ord(letter[ind_let])+int(temp[ind_n])<=ord('z')or ord('A')<=ord(letter[ind_let])+int(temp[ind_n])<=ord('Z'):
            li.append(chr(ord(letter[ind_let])+int(temp[ind_n])))
        elif  ord(letter[ind_let])+int(temp[ind_n])>ord('z'):
            li.append(chr((ord('a')-1)+(int(temp[ind_n])-(ord('z')-ord(letter[ind_let])))))
        elif  ord(letter[ind_let])+int(temp[ind_n])>ord('Z'):
            li.append(chr((ord('A')-1)+(int(temp[ind_n])-(ord('Z')-ord(letter[ind_let])))))  
        ind_n+=1
        ind_let+=1
        if ind_n==len(temp):
            ind_n=0
    print("Encode message is : ",li)                     
def decodemsg(s,n):
    print("Decode message is : ",list(''.join(s.queue).replace(' ','')))    
string,number=input("Enter String and Code : ").split(",")
q1 = Queue(string) 
q2 = Queue(number) 
encodemsg(q1, q2)
decodemsg(q1, q2)
