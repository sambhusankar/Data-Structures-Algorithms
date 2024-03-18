def FixArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == arr[j]:
                arr[i],arr[j]=arr[j],arr[i] 
    print(arr)

FixArray([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1])