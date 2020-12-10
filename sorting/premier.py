def allsort(name,point,gd):
    for i in range(len(point)):
        for j in range(len(point)-1,i,-1):
            if point[j]>point[j-1]:
                point[j],point[j-1]=point[j-1],point[j]
                name[j],name[j-1]=name[j-1],name[j]
                gd[j],gd[j-1]=gd[j-1],gd[j]
            elif point[j]==point[j-1] and gd[j]>gd[j-1]:
                name[j],name[j-1]=name[j-1],name[j]
                gd[j],gd[j-1]=gd[j-1],gd[j]
inp=input('Enter Input : ').split('/')
listgd=[]
listpoint=[]
listname=[]
for i in inp:
    name=i.split(',')[0]
    win=i.split(',')[1]
    draw=i.split(',')[3]
    score=i.split(',')[4]
    conceded=i.split(',')[5]
    point=(3*int(win))+int(draw)
    gd=int(score)-int(conceded)
    listname.append(name)
    listgd.append(gd)
    listpoint.append(point)
allsort(listname,listpoint,listgd)
print('== results ==')
for x in range(len(listpoint)):
    toprint=[]
    toprint.append(listname.pop(0))
    temp={}
    temp['points']=listpoint.pop(0)
    toprint.append(temp)
    tempgd={}
    tempgd['gd']=listgd.pop(0)
    toprint.append(tempgd)
    print(toprint)

