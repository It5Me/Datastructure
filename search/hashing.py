class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)
class hash:
    def __init__(self,size,m):
        self.size=size
        self.li=[None]*size
        self.maxcolision=m
        self.check=0
        self.b=False
    def insert(self,value,key):
        if not self.b:
            sumascii=0
            countcolision=0
            for i in key:
                sumascii+=ord(i)
            position=sumascii%self.size
            if self.li[position]==None:
                self.li[position]=Data(key,value)
                self.check+=1
            else:
                countcolision+=1
                print('collision number {} at {}'.format(countcolision,position))
                j=1
                while self.li[(position+j*j)%self.size]!=None:
                    countcolision+=1
                    print('collision number {} at {}'.format(countcolision,(position+j*j)%self.size))
                    if countcolision==self.maxcolision:
                        print('Max of collisionChain')
                        break
                    j+=1
                if self.li[(position+j*j)%self.size]==None:
                    self.li[(position+j*j)%self.size]=Data(key,value)
                    self.check+=1
            self.toprint()
            if self.check==self.size:
                self.b=True
                print('This table is full !!!!!!') 
    def toprint(self):
        for i in range(len(self.li)):
            print('#{}      {}'.format(i+1,self.li[i]))
        print('---------------------------')
print(' ***** Fun with hashing *****')   
inp=input('Enter Input : ').split('/')
size=int(inp[0].split()[0])
m=int(inp[0].split()[1])
h=hash(size,m)
for i in inp[1].split(','):
    h.insert(i.split()[1],i.split()[0])
