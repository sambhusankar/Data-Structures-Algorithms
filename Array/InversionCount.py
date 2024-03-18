def InversionCount(arr):
    counts=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j] and i < j:
                counts+=1

    print(counts)

InversionCount([1, 20, 6, 4, 5])