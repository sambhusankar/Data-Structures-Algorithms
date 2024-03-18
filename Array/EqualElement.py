def EqualElement(arr,k):
    mxx = max(arr)
    counter = 0
    for i in range(len(arr)):
        if (mxx-arr[i]) % k != 0:
            print(-1)
            break
        else:
            counter+=(mxx-arr[i])/k
    print(counter)
            

EqualElement([4, 7, 19, 16], 3)

