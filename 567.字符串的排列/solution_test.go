//给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
//
// 换句话说，s1 的排列之一是 s2 的 子串 。
//
//
//
// 示例 1：
//
//
//输入：s1 = "ab" s2 = "eidbaooo"
//输出：true
//解释：s2 包含 s1 的排列之一 ("ba").
//
//
// 示例 2：
//
//
//输入：s1= "ab" s2 = "eidboaoo"
//输出：false
//
//
//
//
// 提示：
//
//
// 1 <= s1.length, s2.length <= 10⁴
// s1 和 s2 仅包含小写字母
//
//
// Related Topics 哈希表 双指针 字符串 滑动窗口 👍 967 👎 0

package cn

import (
	"fmt"
	"testing"
)

func TestPermutationInString(t *testing.T) {
	fmt.Println(checkInclusion("bo", "eidbaooo"))
}

// leetcode submit region begin(Prohibit modification and deletion)
func checkInclusion(s1 string, s2 string) bool {
	var windows = make(map[byte]int)
	var need = make(map[byte]int)

	for _, v := range []byte(s1) {
		need[v]++
	}

	var left, right, valid = 0, 0, 0

	for right < len(s2) {
		c := s2[right]
		right++

		if _, ok := need[c]; ok {
			windows[c]++
			if windows[c] == need[c] {
				valid++
			}
		}

		// 如果窗口大于指定字符长度，开始收缩窗口
		for right-left >= len(s1) {
			//
			if valid == len(need) {
				return true
			}
			cc := s2[left]
			left++
			if _, ok := need[cc]; ok {
				if windows[cc] == need[cc] {
					valid--
				}
				windows[cc]--
			}

		}
	}

	return false
}

//leetcode submit region end(Prohibit modification and deletion)
