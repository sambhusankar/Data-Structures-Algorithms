def FindSingle(arr):
    single=[]
    for i in range(len(arr)):
        if arr[i] not in single:
            single.append(arr[i])
        elif arr[i] in single:
            single.remove(arr[i])
        else:
            continue
    print(single)
FindSingle([5,5,9,8,9,8,6,4,4])