def Priority(arr):  
    for i in range(len(arr)):
        count= 0
        for j in range(i,len(arr)):
            if arr[i] == arr[j]:
                count+=1
            if count > len(arr)/2:
                print(arr[i])
                break
Priority([0,0,1,2,3,2,2,2,2,2])