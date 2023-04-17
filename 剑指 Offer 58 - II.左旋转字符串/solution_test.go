//字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数
//将返回左旋转两位得到的结果"cdefgab"。
//
//
//
// 示例 1：
//
// 输入: s = "abcdefg", k = 2
//输出: "cdefgab"
//
//
// 示例 2：
//
// 输入: s = "lrloseumgh", k = 6
//输出: "umghlrlose"
//
//
//
//
// 限制：
//
//
// 1 <= k < s.length <= 10000
//
//
// Related Topics 数学 双指针 字符串 👍 383 👎 0

package cn

import (
	"fmt"
	"testing"
)

func TestZuoXuanZhuanZiFuChuanLcof(t *testing.T) {
	fmt.Println(reverseLeftWords("abcdefg", 2))
}

// leetcode submit region begin(Prohibit modification and deletion)
// 双指针
func reverseLeftWords(s string, n int) string {
	b := []byte(s)
	reverseString(b, 0, n-1)
	reverseString(b, n, len(b)-1)
	reverseString(b, 0, len(b)-1)

	return string(b)
}

func reverseString(b []byte, l, r int) {
	for l < r {
		b[l], b[r] = b[r], b[l]
		l++
		r--
	}
}

//leetcode submit region end(Prohibit modification and deletion)

func reverseLeftWordsV2(s string, n int) string {
	return s[n:] + s[0:n]
}
