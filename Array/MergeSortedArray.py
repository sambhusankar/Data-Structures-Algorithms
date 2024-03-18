def MergeSortedArray(arr1,arr2):
    new_arr=arr1+arr2
    for i in range(len(new_arr)):
        for j in range(i+1,len(new_arr)):
            if new_arr[i] > new_arr[j]:
                new_arr[i],new_arr[j]=new_arr[j],new_arr[i]
    print(new_arr[:len(arr1)],new_arr[len(arr1):])

MergeSortedArray([1, 5, 9, 10, 15, 20],[2, 3, 8, 13])