def PrintLeftRotation(arr,k):
    for i in range(k):
        arr.append(arr.pop(0))
        print(arr)
PrintLeftRotation([1,2,3,4,5],12)