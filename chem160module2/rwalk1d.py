from random import choice
trials=10000
steps=100000
gothome=0
for i in range(trials):
    point=0 #where the walker starts
    for step in range(steps):
        point+=choice((-1,1)) #randomly pick from -1 or 1, and add to point
        if point==0:
            gothome+=1
            break #if this command reaches, jump out of this for loop
print("Fracion that got home=", gothome/trials) #close to 100%
#walkers always get home