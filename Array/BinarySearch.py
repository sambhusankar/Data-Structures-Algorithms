# def Search(arr,key):
#     def FindPivot(l,h):
#         m = int((l+h)/2)
#         if arr[m] < arr[m-1]:
#             return m-1
#         if arr[m] > arr[m+1]:
#             return m
#         if arr[l] < arr[m]:
#             return FindPivot(m,h)
#         if arr[m] > arr[h]:
#             return FindPivot(l,m)
#     p = FindPivot(0,len(arr))
#     def BinarySearch(l,h):
#         print(arr[l:h])
#         m = int((l+h)/2)
#         print(m)
#         if key==arr[m]:
#             print(m)
#         if arr[m] > arr[l]:
#             return BinarySearch(l,m)
#         if arr[m] < arr[h]:
#             return BinarySearch(m,h)


#     if key <= arr[p] and key <= arr[-1]:     
#         BinarySearch(p,len(arr))
#     if key <= arr[p] and key >= arr[0]:
#         BinarySearch(0,p)

#     BinarySearch()
# Search([4,5,6,7,1,2,3,4],2)

def Search(arr, key):
    def FindPivot(l, h):
        m = int((l + h) / 2)
        if arr[m] < arr[m - 1]:
            return m - 1
        if arr[m] > arr[m + 1]:
            return m
        if arr[l] < arr[m]:
            return FindPivot(m, h)
        if arr[m] > arr[h]:
            return FindPivot(l, m)
    p = FindPivot(0, len(arr) )
    def BinarySearch(l, h):
         m = int((l + h) / 2)
         if key==arr[m]:
             print(m)
         if arr[m] > key:
             return BinarySearch(l,m)
         if arr[m] < key:
             return BinarySearch(m,h)

    if key <= arr[p] and key <= arr[-1]:     
         BinarySearch(p,len(arr))
    if key <= arr[p] and key >= arr[0]:
         BinarySearch(0,p)


# Example usage
Search([4, 5, 6, 1, 2, 3 , 4], 2)
