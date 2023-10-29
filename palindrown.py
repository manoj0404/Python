li = [5,6,7,10,5]
length =len(li)
#mid = (s+e)//2
for i in range(length//2):
    if(li[i]!=li[length-i-1]):
        print("no")
    else:
        print("yes")
