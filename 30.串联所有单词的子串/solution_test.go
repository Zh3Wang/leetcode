//给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。
//
// s 中的 串联子串 是指一个包含 words 中所有字符串以任意顺序排列连接起来的子串。
//
//
// 例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，
//"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
//
//
// 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。
//
//
//
// 示例 1：
//
//
//输入：s = "barfoothefoobarman", words = ["foo","bar"]
//输出：[0,9]
//解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
//子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
//子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
//输出顺序无关紧要。返回 [9,0] 也是可以的。
//
//
// 示例 2：
//
//
//输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
//输出：[]
//解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
//s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
//所以我们返回一个空数组。
//
//
// 示例 3：
//
//
//输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
//输出：[6,9,12]
//解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
//子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
//子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
//子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
//
//
//
// 提示：
//
//
// 1 <= s.length <= 10⁴
// 1 <= words.length <= 5000
// 1 <= words[i].length <= 30
// words[i] 和 s 由小写英文字母组成
//
//
// Related Topics 哈希表 字符串 滑动窗口 👍 1030 👎 0

package cn

import (
	"fmt"
	"testing"
)

func TestSubstringWithConcatenationOfAllWords(t *testing.T) {
	fmt.Println(findSubstring("ababaab", []string{"ab", "ba", "ba"}))
}

// leetcode submit region begin(Prohibit modification and deletion)
func findSubstring(s string, words []string) []int {
	var need = make(map[string]int)
	step := 0
	for _, v := range words {
		step = len(v)
		need[v]++
	}

	// 把每个word当成一个byte来看待，窗口滑动的步长调整为word的长度step
	// 因为步长为step，则总共有step种滑动起始位置，比如step=3，则分别需要从0，1，2三个位置开始滑动窗口
	// 所以这里需要分step组开滑
	var res = make([]int, 0)
	for i := 0; i < step; i++ {
		var left, right, valid = i, i, 0
		var windows = make(map[string]int)

		for right <= len(s)-step {
			// 每次遍历一个单词
			c := s[right : right+step]
			right += step

			if _, ok := need[c]; ok {
				windows[c]++
				if windows[c] == need[c] {
					valid++
				}
			}

			// 当窗口大于所有单词的长度时，开始收缩
			for right-left >= len(words)*step {
				if valid == len(need) {
					res = append(res, left)
				}

				cc := s[left : left+step]
				if _, ok := need[cc]; ok {
					if windows[cc] == need[cc] {
						valid--
					}
					windows[cc]--
				}
				left += step
			}
		}
	}

	return res
}
func findSubstringV2(s string, words []string) []int {
	var need = make(map[string]int)

	step := 0
	for _, v := range words {
		need[v]++
		step = len(v)
	}

	var res = make([]int, 0)
	for i := 0; i < step; i++ {
		var windows = make(map[string]int)
		var left, right, valid = i, i, 0

		for right < len(s)-step+1 {
			c := s[right : right+step]
			right += step

			if _, ok := need[c]; ok {
				windows[c]++
				if windows[c] == need[c] {
					valid++
				}
			}

			for right-left >= len(words)*step {
				if valid == len(need) {
					res = append(res, left)
				}

				cc := s[left : left+step]
				if _, ok := need[cc]; ok {
					if windows[cc] == need[cc] {
						valid--
					}
					windows[cc]--
				}

				left += step
			}
		}
	}

	return res
}

//leetcode submit region end(Prohibit modification and deletion)
