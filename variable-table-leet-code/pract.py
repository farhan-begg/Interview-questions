def kLargest(arr, k):
    # Sort the given array arr in reverse
    # order.
    arr.sort(reverse=True)
    # Print the first kth largest elements
    for i in range(k):
        print(arr[i], end=" ")


# Driver program
arr = [1, 23, 12, 9, 30, 2, 50]
# n = len(arr)
k = 3
kLargest(arr, k)

'''

variable table 
arr = [1, 23, 12, 9, 30, 2, 50]
arr = [1,2,9, 12, 23, 50]
k = 3


'''
