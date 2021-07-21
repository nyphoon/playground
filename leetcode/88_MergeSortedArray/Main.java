// 88. Merge Sorted Array
// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
// and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
// Merge nums1 and nums2 into a single array sorted in non-decreasing order.
// The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
// To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
// and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

// Example 1:
// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
// Output: [1,2,2,3,5,6]
// Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
// The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
// Example 2:
// Input: nums1 = [1], m = 1, nums2 = [], n = 0
// Output: [1]
// Explanation: The arrays we are merging are [1] and [].
// The result of the merge is [1].
// Example 3:
// Input: nums1 = [0], m = 0, nums2 = [1], n = 1
// Output: [1]
// Explanation: The arrays we are merging are [] and [1].
// The result of the merge is [1].
// Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
// Constraints:
// nums1.length == m + n
// nums2.length == n
// 0 <= m, n <= 200
// 1 <= m + n <= 200

import java.io.*;

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Merge Sorted Array.
// Memory Usage: 39.7 MB, less than 7.67% of Java online submissions for Merge Sorted Array.
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int cur1 = m - 1;
        int cur2 = n - 1;
        for(int i=m+n-1; i>=0; i--){
            if(cur1<0){
                nums1[i] = nums2[cur2];
                cur2--;
            }else if(cur2<0){
                nums1[i] = nums1[cur1];
                cur1--;
            }else if(nums1[cur1] > nums2[cur2]){
                nums1[i] = nums1[cur1];
                cur1--;
            }else{
                nums1[i] = nums2[cur2];
                cur2--;
            }
        }
    }
}


public class Main { 
    public static void main(String args[]) { 
        var s = new Solution();

        // int[] nums1 = {1,2,3,0,0,0};
        // int[] nums2 = {2,5,6};
        // s.merge(nums1, 3, nums2, 3);

        int[] nums1 = {0};
        int[] nums2 = {2};
        s.merge(nums1, 0, nums2, 1);

        for(int n : nums1){
            System.out.println(n);
        }
    } 
}