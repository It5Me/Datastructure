class Queue:
    def __init__(self, li=None):
        if li == None:
            self.queue = []
        else:
            self.queue = li

    def enqueue(self, items):
        self.queue.append(items)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(', '.join(self.queue))


def checklo(lo):
    if lo == '0':
        return "Res."
    elif lo == '1':
        return "ClassR."
    elif lo =='2':
        return "SuperM."
    elif lo=='3':
        return "Home"
def checkact(act):
    if act == '0':
        return "Eat"
    elif act == '1':
        return "Game"
    elif act =='2':
        return "Learn"
    elif act=='3':
        return "Movie"                    
inp=input("Enter Input : ").split(",")
itme=Queue()
ityou=Queue()
score=0
ili=[]
uli=[]
for x in inp:
    itme.enqueue(x.split()[0])
    ityou.enqueue(x.split()[1])

print("My   Queue =",itme)
print("Your Queue =",ityou)
temp=[]
num=0
print("My   Activity:Location = ",end="")
for i in itme.queue:
    temp=i.split(', ')
    act=temp[0].split(':')[0]
    lo=temp[0].split(':')[1]
    print(checkact(act)+':'+checklo(lo),end="")
    num+=1
    if num< itme.size():
        print(", ",end="")
    else:
        print("")
print("Your Activity:Location = ",end="")
num2=0        
for i in ityou.queue:
    temp=i.split(', ')
    temp=i.split(', ')
    act=temp[0].split(':')[0]
    lo=temp[0].split(':')[1]
    print(checkact(act)+':'+checklo(lo),end="")
    num2+=1
    if num2< ityou.size():
        print(", ",end="")
    else:
        print("")

while itme.size()>0 and ityou.size()>0:
    it=[]
    u=[]
    it=itme.dequeue().split(':')
    u=ityou.dequeue().split(':')
    if it[0]==u[0]:
        if it[1]==u[1]:
            score+=4                
        else:
            score+=1        
    elif it[1]==u[1]:
        if it[0]!=u[0]:
            score+=2        
    else:
        score-=5                
if score>=7:
    print("Yes! You're my love! : Score is {}.".format(score))
elif score>0:
    print("Umm.. It's complicated relationship! : Score is {}.".format(score))
else:
    print("No! We're just friends. : Score is {}.".format(score))    
      







