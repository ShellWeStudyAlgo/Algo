class Solution {
    public int searchInsert(int[] nums, int target) {
        // 변수 초기화
        int result = 0;
        int n = nums.length;
        // 바이너리 서치 시작
        while (result < n) {
            // 중간값 계산
            final int mid = (result + n) / 2;
            // 중간값이 타겟과 같으면 중간 인덱스 반환
            if (nums[mid] == target)
                return mid;
            // 중간값이 타겟보다 작으면 범위를 오른쪽으로 좁힘
            if (nums[mid] < target)
                result = mid + 1;
            // 중간값이 타겟보다 크면 범위를 왼쪽으로 좁힘
            else
                n = mid;
        }
        // 타겟이 없는 경우 삽입될 위치 반환
        return result;
    }
}
