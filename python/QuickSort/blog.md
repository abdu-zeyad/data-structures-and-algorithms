# Merge Sort

QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

Pseudocode:
 QuickSort(arr, left, right)
 if left < right
        DEFINE position <-- Partition(arr, left, right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1, right)
ALGORITHM Partition(arr, left, right)
    DEFINE pivot <-- arr[right]
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1
ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
Trace:

- Sample Array: [8,4,23,42,16]

Pass 1:

Pass 1 of quick Sort

In the first pass through of the merge sort, divide the array into 2 arrays, then iterate tis process until the 2 arrays are only one element, compare between them and assign the first element of the new array with the lowest and the other element as the second element.
[4,8] and the other elements are [23,45,16]
Pass 2:

Pass 2 of quick Sort

The second pass is to merge the left and the right sides, compare each element to sort them from the lowest to the highest.
Pass 3:

Pass 3 of quick Sort

The third pass merge the entire new array and return it.
[4,8,16,32,42]
Efficiency

- Time: O(n^2)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
- Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).
