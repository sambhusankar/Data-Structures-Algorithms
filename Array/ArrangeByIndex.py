def ArrangeByIndex(arr,ind):
    output = len(ind) * [0]
    for i in range(len(ind)):
        output[ind[i]] = arr[i]

    print(output)

ArrangeByIndex([50, 40, 70, 60, 90],[3,  0,  4,  1,  2])