def SecondLarge(arr):
    sec_large= 0
    large=sec_large+1
    
    for i in range(len(arr)):
        if arr[i] > arr[large]:
            sec_large = i
            
    print(sec_large)
SecondLarge([7,2,4,3,5,9])