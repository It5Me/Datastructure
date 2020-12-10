n = [9,3,8,6,2,7,1]
m_ax=0
count=0

for x in n[::-1]:
    if x>m_ax:
        m_ax=x
        count+=1
print(count)        