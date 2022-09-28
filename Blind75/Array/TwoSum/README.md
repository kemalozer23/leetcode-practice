## Approach(Two Pointer)

The given array is sorted. This is a special case because we know that if we have fixed a first index then the required value to fulfill the target an be found ahead in the array using binary search. 

A similar approach can be used: We can use two pointers: left and right, intially at the first and the last element of the array respectively. We can then compare the sum of these two pointer values to the target. If the sum of values and target are equal, then we have found the only solution. So, we return this index pair. Otherwise, if the sum of values is less than the target, we need to increment or dec rement one of the pointers. Obviously, we are bringing the right pointer from the end only. So, we should increment the left pointer and check for the same condition. Similarly, if sum of values is more than target, we decrement the right pointer.

![alt text](https://www.tutorialcup.com/wp-content/uploads/2020/12/targetSum-e1607845835473.png?ezimgfmt=rs:607x336/rscb41/ng:webp/ngcb41)