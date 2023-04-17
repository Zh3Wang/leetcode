//给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
//
// 如果数组中不存在目标值 target，返回 [-1, -1]。
//
// 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
//
//
//
// 示例 1：
//
//
//输入：nums = [5,7,7,8,8,10], target = 8
//输出：[3,4]
//
// 示例 2：
//
//
//输入：nums = [5,7,7,8,8,10], target = 6
//输出：[-1,-1]
//
// 示例 3：
//
//
//输入：nums = [], target = 0
//输出：[-1,-1]
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
// Related Topics 数组 二分查找 👍 2259 👎 0

package cn

import (
	"fmt"
	"testing"
)

func TestFindFirstAndLastPositionOfElementInSortedArray(t *testing.T) {
	a := searchRange([]int{}, 0)
	fmt.Println(a)
}

// leetcode submit region begin(Prohibit modification and deletion)
func searchRange(nums []int, target int) []int {
	var start, end = -1, -1
	// 查找最左边界值
	var left, right = 0, len(nums) - 1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	if left < len(nums) && nums[left] == target {
		start = left
	}

	// 最右
	left, right = 0, len(nums)-1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			left = mid + 1
		}
	}

	if right >= 0 && nums[right] == target {
		end = right
	}

	return []int{start, end}
}

//leetcode submit region end(Prohibit modification and deletion)

func searchRangeV2(nums []int, target int) []int {
	var left, right = 0, len(nums) - 1
	var start, end = -1, -1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			a := mid
			for a < len(nums) && nums[a] == target {
				a++
			}
			end = a - 1
			b := mid
			for b >= 0 && nums[b] == target {
				b--
			}
			start = b + 1
			break
		}
	}

	return []int{start, end}
}
