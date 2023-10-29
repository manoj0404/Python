li = list(map(int,input().split()))
key = int(input())
s= 0
e = len(li)-1
while s<=e:
    mid = (s+e)//2
    if li[mid]==key:
        print(f" Element is present at {mid}")
        break
    elif key>mid:
        s = mid+1
    else:
        e = mid-1
else:
    print("Not present")