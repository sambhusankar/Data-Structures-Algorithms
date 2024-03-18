def Leaders(arr):
    leaders=[]
    leader = False
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                leader = True
            else:
                leader = False
                break

        if leader == True:
            leaders.append(arr[i])
    print(leaders)
Leaders([16, 17, 4, 3, 5, 2])
                

