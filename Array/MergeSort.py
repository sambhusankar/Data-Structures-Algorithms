def _mergeSort(arr, temp_arr, left, right):
 
    # A variable inv_count is used to store
    # inversion counts in each recursive call
 
    inv_count = 0
 
    # We will make a recursive call if and only if
    # we have more than one elements
 
    if left < right:
 
        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python
 
        mid = (left + right)//2
 
        # It will calculate inversion
        # counts in the left subarray
 
        inv_count += _mergeSort(arr, temp_arr,
                                left, mid)
 
        # It will calculate inversion
        # counts in right subarray
 
        inv_count += _mergeSort(arr, temp_arr,
                                mid + 1, right)
 
        # It will merge two subarrays in
        # a sorted subarray
 
        #inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

a = _mergeSort([8, 4, 2, 1],[0,0,0,0],0,3)
print(a)