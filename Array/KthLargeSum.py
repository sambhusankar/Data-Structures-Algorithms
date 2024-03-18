def KthLargeSum(arr,k):
    new_arr=[]
    for i in range(len(arr)):
        items=0
        for j in range(i,len(arr)):
            items+=arr[j]
            
            new_arr.append(items)
 
    for i in range(len(new_arr)-1):
        for j in range(i+1,len(new_arr)):
            if new_arr[i] > new_arr[j]:
                new_arr[j],new_arr[i]=new_arr[i],new_arr[j]
    print(new_arr)
        
    

KthLargeSum([10, -10, 20, -40],6)