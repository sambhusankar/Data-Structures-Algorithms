def UpdateArray(arr,l,r,x):
    for i in range(l,r+1):
        arr[i]+= x
    return arr
def PrintArray(arr):
    print(arr)

a=[0,0,0,0]
UpdateArray(a,0,2,10)
UpdateArray(a,3,3,10)
PrintArray(a)