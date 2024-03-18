def Triangle(arr):
    counter = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j] > arr[k] and arr[i]+arr[k] > arr[j] and arr[k]+arr[j] > arr[i]:
                    counter+=1
    print(counter)

Triangle([10, 21, 22, 100, 101, 200, 300])