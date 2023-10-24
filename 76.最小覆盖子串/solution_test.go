//给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
//
//
//
// 注意：
//
//
// 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
// 如果 s 中存在这样的子串，我们保证它是唯一的答案。
//
//
//
//
// 示例 1：
//
//
//输入：s = "ADOBECODEBANC", t = "ABC"
//输出："BANC"
//解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
//
//
// 示例 2：
//
//
//输入：s = "a", t = "a"
//输出："a"
//解释：整个字符串 s 是最小覆盖子串。
//
//
// 示例 3:
//
//
//输入: s = "a", t = "aa"
//输出: ""
//解释: t 中两个字符 'a' 均应包含在 s 的子串中，
//因此没有符合条件的子字符串，返回空字符串。
//
//
//
// 提示：
//
//
// m == s.length
// n == t.length
// 1 <= m, n <= 10⁵
// s 和 t 由英文字母组成
//
//
//
//进阶：你能设计一个在
//o(m+n) 时间内解决此问题的算法吗？
//
// Related Topics 哈希表 字符串 滑动窗口 👍 2466 👎 0

package cn

import (
	"fmt"
	"math"
	"testing"
)

func TestMinimumWindowSubstring(t *testing.T) {
	a := minWindow("ADOBECODEBANC", "ABC")
	fmt.Println(a)
}

// leetcode submit region begin(Prohibit modification and deletion)
func minWindow(s string, t string) string {
	var need = make(map[byte]int)
	var window = make(map[byte]int)

	for _, v := range []byte(t) {
		need[v]++
	}

	var left, right, valid = 0, 0, 0
	var start, end = 0, math.MaxInt32

	for right < len(s) {
		c := s[right]
		right++

		if _, ok := need[c]; ok {
			window[c]++
			if window[c] == need[c] {
				valid++
			}
		}

		for valid >= len(need) {
			cc := s[left]
			if right-left < end-start {
				start, end = left, right
			}
			if _, ok := need[cc]; ok {
				if window[cc] == need[cc] {
					valid--
				}
				window[cc]--
			}
			left++
		}
	}

	if start == 0 && end == math.MaxInt32 {
		return ""
	}

	return s[start:end]
}

func minWindowV2(s string, t string) string {
	var need = make(map[byte]int)
	var window = make(map[byte]int)

	for i := range t {
		need[t[i]]++
	}

	var left, right, valid int
	var start, end = 0, math.MaxInt32
	for right < len(s) {
		c := s[right]
		right++

		if _, ok := need[c]; ok {
			window[c]++
			if window[c] == need[c] {
				valid++
			}
		}

		for valid >= len(need) {
			cc := s[left]
			if right-left < end-start {
				start, end = left, right
			}
			if _, ok := need[cc]; ok {
				if window[cc] == need[cc] {
					valid--
				}
				window[cc]--
			}

			left++
		}

	}
	if start == 0 && end == math.MaxInt32 {
		return ""
	}

	return s[start:end]
}

//leetcode submit region end(Prohibit modification and deletion)
