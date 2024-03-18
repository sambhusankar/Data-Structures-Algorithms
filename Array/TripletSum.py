def TripletSum(arr,z):
    for i in range(len(arr)-2):
        current_sum=z-arr[i]
        for j in range(i+1,len(arr)):
            required_value=current_sum-arr[j]
            if required_value in arr:
                print(arr[i],arr[j],required_value)
                break
    
TripletSum([1, 2, 3, 4, 5],9)