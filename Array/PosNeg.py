def PosNeg(arr):
    i = -1
    for j in range(len(arr)):
        if arr[j] < 0:
            i +=1
            arr[j],arr[i]=arr[i],arr[j]

    pos,neg=i+1,0
    while(pos < len(arr) and neg < pos and arr[neg] < 0):
        arr[neg],arr[pos] = arr[pos],arr[neg]
        pos+=1
        neg+=2
    print(arr)
PosNeg([-1, 2, -3, 4, 5, 6, -7, 8, 9])