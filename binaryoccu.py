li = list(map(int,input().split()))
key = int(input())
s= 0
e = len(li)-1
ans = -1
while s<=e:
    mid = (s+e)//2
    if li[mid]==key:
        ans = mid
        break
    elif li[mid]<key:
        s = mid+1
    else:
        e = mid-1
print(ans)