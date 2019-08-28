from random import choice
dim=6 #specifies dimension for random walker test
trials=1000
steps=10000
gothome=0
for i in range(trials):
    point=[0]*dim #multiply list by dimension present
    for step in range(steps):
        for j in range(dim): #loop over number of dimensions
            point[j]+=choice((-1,1)) #point is a list, so add brackets
        if point.count(0)==dim: #count function counts number of zeros in vector point
            gothome+=1
            break
print("Fracion that got home=%f in %d dims"%(gothome/trials,dim))