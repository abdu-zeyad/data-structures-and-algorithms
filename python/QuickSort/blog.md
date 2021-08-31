# Merge Sort

Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

Pseudocode:

Mergesort(arr)
    DECLARE n <-- arr.length
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      Mergesort(left)
      Mergesort(right)
      Merge(left, right, arr)

Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0
    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

Trace:

- Sample Array: [8,4,23,42,16]

Pass 1:

Pass 1 of Insertion Sort

In the first pass through of the merge sort, divide the array into 2 arrays, then iterate tis process until the 2 arrays are only one element, compare between them and assign the first element of the new array with the lowest and the other element as the second element.
[4,8] and the other elements are [23,45,16]
Pass 2:

Pass 2 of Insertion Sort

The second pass is to merge the left and the right sides, compare each element to sort them from the lowest to the highest.
Pass 3:

Pass 3 of Insertion Sort

The third pass merge the entire new array and return it.
[4,8,16,32,42]
Efficiency

- Time: O(n^2)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
- Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).
