def Equalibrium(arr):
    for i in range(1,len(arr)-1):
        print(arr[:i])
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
e= Equalibrium([-7, 1, 5, 2, -4, 3, 0])
print(e)