def SmallestSubarrySum(arr,x):
    sum=0
    for i in range(len(arr)):
        sum+= arr[i]
        if sum > x:
            print(i)
            break
SmallestSubarrySum([1, 11, 100, 1, 0, 200, 3, 2, 1, 250],280)