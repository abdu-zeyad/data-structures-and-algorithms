# Insertion Sort

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

Pseudocode:

  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

Trace:

- Sample Array: [8,4,23,42,16,15]

Pass 1:

Pass 1 of Insertion Sort

In the first pass through of the Insertion sort, we
start with the second element in the array, and compare it with the previous element,if the second element is lower than the previous element, the values will be swapped so the first element will be 4 and the second is 8.

Pass 2:

Pass 2 of Insertion Sort

The second pass through the array evaluates the third element with the second element which in this case the third element is higher then the second element. therefore, the third element stays in its position.
[4,8,23]
Pass 3:

Pass 3 of Insertion Sort

The third pass through evaluates the remaining indexes in the array, is similar to the second pass,
the value of the forth element is higher than the third element. therefore it stays in its position as well.
[4,8,23,42]

Pass 4:

Pass 4 of Insertion Sort

The 4th pass through on the array proves that 16 is lower than the previous value, so the the value of the index 5 is assigned to the previous value, and the index is decremented by one, and do the comparison again with the value 23 which is again higher than 16, we assign the value of the index 16 to 23 and decrement the index by 1, and do the comparison again, at this moment 16 is higher than 8, so it stays in its position.
[4,8,16,23,42]
Pass 5:

Pass 5 of Insertion Sort

doing the same criteria in pass 4 leads to the final sorted array.
[4,8,15,16,23,42]

Efficiency

- Time: O(n^2)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
- Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).
