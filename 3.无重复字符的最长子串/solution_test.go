//给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
//
//
//
// 示例 1:
//
//
//输入: s = "abcabcbb"
//输出: 3
//解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
//
//
// 示例 2:
//
//
//输入: s = "bbbbb"
//输出: 1
//解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
//
//
// 示例 3:
//
//
//输入: s = "pwwkew"
//输出: 3
//解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
//     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
//
//
//
//
// 提示：
//
//
// 0 <= s.length <= 5 * 10⁴
// s 由英文字母、数字、符号和空格组成
//
//
// Related Topics 哈希表 字符串 滑动窗口 👍 9082 👎 0

package cn

import (
	"fmt"
	"testing"
)

func TestLongestSubstringWithoutRepeatingCharacters(t *testing.T) {
	s := "pwwkew"
	fmt.Println(lengthOfLongestSubstring(s))
}

// leetcode submit region begin(Prohibit modification and deletion)
func lengthOfLongestSubstring(s string) int {
	var window = make(map[byte]int)

	var left, right, ans int
	for right < len(s) {
		c := s[right]
		right++
		window[c]++
		if window[c] == 1 && right-left > ans {
			ans = right - left
		}

		for window[c] > 1 {
			cc := s[left]
			window[cc]--
			left++
		}

	}

	return ans
}

//leetcode submit region end(Prohibit modification and deletion)
