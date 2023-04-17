//统计一个数字在排序数组中出现的次数。
//
//
//
// 示例 1:
//
//
//输入: nums = [5,7,7,8,8,10], target = 8
//输出: 2
//
// 示例 2:
//
//
//输入: nums = [5,7,7,8,8,10], target = 6
//输出: 0
//
//
//
// 提示：
//
//
// 0 <= nums.length <= 10⁵
// -10⁹ <= nums[i] <= 10⁹
// nums 是一个非递减数组
// -10⁹ <= target <= 10⁹
//
//
//
//
// 注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
//position-of-element-in-sorted-array/
//
// Related Topics 数组 二分查找 👍 415 👎 0

package cn

import (
	"fmt"
	"testing"
)

func TestZaiPaiXuShuZuZhongChaZhaoShuZiLcof(t *testing.T) {
	fmt.Println(search([]int{1, 1, 2}, 1))
}

// leetcode submit region begin(Prohibit modification and deletion)
func search(nums []int, target int) int {
	var left, right, counter = 0, len(nums) - 1, 0
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			counter++
			a := mid - 1
			for a >= 0 && nums[a] == target {
				counter++
				a--
			}

			b := mid + 1
			for b < len(nums) && nums[b] == target {
				counter++
				b++
			}
			break
		}
	}
	return counter
}

//leetcode submit region end(Prohibit modification and deletion)
