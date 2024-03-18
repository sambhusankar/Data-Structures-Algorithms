def SubArraySum(arr,sum):
    for j in range(len(arr)):
        s = 0
        for i in range(j,len(arr)):
            s+= arr[i]
            if s == sum:
                print(arr[j:i+1])
            
          
SubArraySum([1, 4, 20, 3, 10, 5],33)