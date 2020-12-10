def rehash():
    pass

print(" ***** Rehashing *****")
inp,data=input("Enter Input : ").split('/')
print("Initial Table :")
table=inp.split()[0]
maxcollision=inp.split()[1]
threshold=inp.split()[2]
for i in data:
    