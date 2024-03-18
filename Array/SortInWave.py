def SortInWave(arr):
    arr.sort()
    for i in range(0,len(arr)-1,2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    print(arr)
SortInWave([2,3,1,5,4,9,6])