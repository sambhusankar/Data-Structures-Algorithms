def MaxMin(arr):
    max= len(arr)-1
    min=0
    output=[]
    flag = True
    for i in range(len(arr)):
        if flag is True:
            output.append(arr[max])
            max-=1
            flag = False
        else:
            output.append(arr[min])
            min+=1
            flag = True
    print(output)
MaxMin([1,2,3,4,5])