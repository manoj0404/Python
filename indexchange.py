li = [-1,2,4,5,0,-5,-6]
li1=[]
li2=[]
for i in li:
    if(i<0):
        li1.append(i)
    elif(i==0):
        li2.append(i)
    else:
        li.append(i)
print(li)
print(li1)
print(li2)