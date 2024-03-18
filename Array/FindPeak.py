def FindPeak(arr):
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            print(arr[i])

FindPeak([10, 20, 15, 2, 23, 90, 67])