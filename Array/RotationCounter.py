def RotationCounter(arr):
    c = 0
    while c < len(arr)-1:
        if arr[c] < arr[c+1] and c+1 != len(arr):
             c+=1            
        else:
            break
    if c+1 == len(arr):
        print(0)
    else:
        print(c+1)

RotationCounter([15, 18, 2, 3, 6, 12])