def TwoPointer(arr,x):
    m=0;n=len(arr)-1
    while m < n:
        if arr[m] + arr[n] ==  x:
            print(arr[m],arr[n])
        if arr[m] + arr[n] < x:
            m+=1
        else:
            n-=1
    
TwoPointer([2, 3, 5, 8, 9, 10, 11],17)