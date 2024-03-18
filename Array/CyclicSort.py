def CyclicSort(arr):
    for i in range(len(arr)):
        while arr[i] != i+1:
            temp= arr[i]
            arr[i],arr[temp-1] =arr[arr[i]-1],temp    
    print(arr)
CyclicSort([4,5,8,7,1,2,3,6])


