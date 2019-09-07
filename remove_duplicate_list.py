a=[1, 2, 3, 1, 5, 2, 4, 4, 5]
l=len(a)
l=l-1
while(l>=0):
    first=a[l]
    l=l-1
    j=l
    while(j>=0):
        second=a[j]
        if first==second:
            a.remove(a[j])
        j=j-1
print(a)
        
