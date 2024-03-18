def EvenOdd(arr):
    even=[]
    odd = []
    for i in range(len(arr)):
        if arr[i]%2 == 0: 
            even.append(arr[i])
        else:
            odd.append(arr[i])
    print(even+odd)
EvenOdd([1,4,3,2,5,6,7])
