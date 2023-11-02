//给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i
//- j) <= k 。如果存在，返回 true ；否则，返回 false 。
//
//
//
// 示例 1：
//
//
//输入：nums = [1,2,3,1], k = 3
//输出：true
//
// 示例 2：
//
//
//输入：nums = [1,0,1,1], k = 1
//输出：true
//
// 示例 3：
//
//
//输入：nums = [1,2,3,1,2,3], k = 2
//输出：false
//
//
//
//
//
// 提示：
//
//
// 1 <= nums.length <= 10⁵
// -10⁹ <= nums[i] <= 10⁹
// 0 <= k <= 10⁵
//
//
// Related Topics 数组 哈希表 滑动窗口 👍 650 👎 0

package cn

import (
	"fmt"
	"math"
	"testing"
)

func TestContainsDuplicateIi(t *testing.T) {
	fmt.Println(containsNearbyDuplicate([]int{99, 99}, 2))
}

// leetcode submit region begin(Prohibit modification and deletion)
// 滑动窗口
// 保证窗口的长度为（i-k, i）,即长度为k+1， 在窗口内如果出现重复元素，两者坐标之差一定小于等于k，则返回true
func containsNearbyDuplicate(nums []int, k int) bool {
	var windows = make(map[int]struct{})
	for i, num := range nums {
		if i > k {
			delete(windows, nums[i-k-1])
		}

		if _, ok := windows[num]; ok {
			return true
		}

		windows[num] = struct{}{}
	}
	return false
}

// 哈希表解法
func containsNearbyDuplicateHash(nums []int, k int) bool {
	var mp = make(map[int]int)
	for i, v := range nums {
		if j, ok := mp[v]; ok {
			if math.Abs(float64(j-i)) <= float64(k) {
				return true
			}
		}
		mp[v] = i
	}
	return false
}

//leetcode submit region end(Prohibit modification and deletion)
