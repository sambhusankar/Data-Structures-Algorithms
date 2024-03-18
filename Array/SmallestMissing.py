def SmallestMissing(arr,m):
    for i in range(len(arr)):
        if arr[i] != i:
            print(i)
            break
        if i ==len(arr)-1:
            print(i+1)
SmallestMissing([ 0, 1, 2, 4 ],5)