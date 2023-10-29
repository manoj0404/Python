li = list(map(int,input().split()))
print(li)
key = int(input("Enter the no:"))
for i in range(len(li)):
    if li[i] == key:
        print(i)
    