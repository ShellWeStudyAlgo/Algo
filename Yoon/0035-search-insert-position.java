class Solution {
    public int searchInsert(int[] nums, int target) {
        
        int result = 0;
        int n = nums.length;

        while (result < n) {
            final int mid = (result + n) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] < target)
                result = mid + 1;
            else
                n = mid;
        }
        return result;
    }
}