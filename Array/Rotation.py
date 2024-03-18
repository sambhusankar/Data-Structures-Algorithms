def Rotation(arr,d):
    for i in range(d):
        a= arr.pop(0)
        arr.append(a)
        print(arr)
Rotation([1,2,3,4,5],3)