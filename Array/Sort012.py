def Sort012(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j]=arr[j],arr[i]

    print(arr)
Sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])