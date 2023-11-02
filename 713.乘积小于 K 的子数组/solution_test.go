//给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
//
//
//
// 示例 1：
//
//
//输入：nums = [10,5,2,6], k = 100
//输出：8
//解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
//需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
//
//
// 示例 2：
//
//
//输入：nums = [1,2,3], k = 0
//输出：0
//
//
//
// 提示:
//
//
// 1 <= nums.length <= 3 * 10⁴
// 1 <= nums[i] <= 1000
// 0 <= k <= 10⁶
//
//
// Related Topics 数组 滑动窗口 👍 741 👎 0

package cn

import (
	"fmt"
	"testing"
)

func TestSubarrayProductLessThanK(t *testing.T) {
	fmt.Println(numSubarrayProductLessThanK([]int{10, 5, 2, 6}, 100))
}

// leetcode submit region begin(Prohibit modification and deletion)
func numSubarrayProductLessThanK(nums []int, k int) int {
	return 0
}

func numSubarrayProductLessThanKV2(nums []int, k int) int {
	var left, right, pre, res = 0, 0, 1, 0
	for right < len(nums) {
		pre *= nums[right]
		for pre >= k && left <= right {
			pre /= nums[left]
			left++
		}
		right++
		// 关键是这个累加：窗口每往右滑动一位，则符合条件的结果会增加（当前窗口长度）的数量
		res += right - left
	}
	return res
}

//leetcode submit region end(Prohibit modification and deletion)
