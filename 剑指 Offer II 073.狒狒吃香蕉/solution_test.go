//狒狒喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。
//
// 狒狒可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后
//这一小时内不会再吃更多的香蕉，下一个小时才会开始吃另一堆的香蕉。
//
// 狒狒喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
//
// 返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。
//
//
//
//
//
//
// 示例 1：
//
//
//输入：piles = [3,6,7,11], h = 8
//输出：4
//
//
// 示例 2：
//
//
//输入：piles = [30,11,23,4,20], h = 5
//输出：30
//
//
// 示例 3：
//
//
//输入：piles = [30,11,23,4,20], h = 6
//输出：23
//
//
//
//
// 提示：
//
//
// 1 <= piles.length <= 10⁴
// piles.length <= h <= 10⁹
// 1 <= piles[i] <= 10⁹
//
//
//
//
//
// 注意：本题与主站 875 题相同： https://leetcode-cn.com/problems/koko-eating-bananas/
//
// Related Topics 数组 二分查找 👍 56 👎 0

package cn

import (
	"fmt"
	"testing"
)

func TestNZZqjQ(t *testing.T) {
	a := minEatingSpeed([]int{312884470}, 312884469)
	fmt.Println(a)
}

// leetcode submit region begin(Prohibit modification and deletion)
func minEatingSpeed(piles []int, h int) int {
	if h < len(piles) {
		return -1
	}
	left, right := 1, 0
	for _, v := range piles {
		right = max(right, v)
	}

	var res = 0
	for left <= right {
		mid := left + (right-left)/2
		t := eatSpendTime(piles, mid)
		if t <= h {
			res = mid
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return res
}

// 计算指定速度吃完所有香蕉要花多久时间
func eatSpendTime(piles []int, speed int) int {
	var t int
	for _, p := range piles {
		v, mod := p/speed, p%speed
		if mod > 0 {
			v++
		}
		t += v
	}
	return t
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

//leetcode submit region end(Prohibit modification and deletion)
