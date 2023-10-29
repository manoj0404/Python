li = [i for i in range(10)]
li1= [0]*10
print(li)
j=0
for i in range(len(li)-1,-1,-1):
  li1[j] = li[i]
  j+=1
print(li1)