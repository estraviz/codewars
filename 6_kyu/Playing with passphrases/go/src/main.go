// Playing with passphrases
package kata

import (
	"strconv"
	"strings"
	"unicode"
)

func PlayPass(s string, n int) string {
    var str, ch string
    for i, r := range s {
        if unicode.IsLetter(r) {
            ch = string(shiftN(r, n))
            if i % 2 == 0 {
                ch = strings.ToUpper(ch)
            } else {
                ch = strings.ToLower(ch)
            }
        } else if unicode.IsNumber(r) {
            ch = strconv.Itoa(complementN(r, 9))
        } else {
            ch = string(r)
        }
        str += ch
    }
    return getReversed(str)
}

func complementN(r rune, N int) int {
    num, _ := strconv.Atoi(string(r))
    return N - num
}

func shiftN(r rune, N int) rune {
    s := int(r) + N
    if unicode.IsLower(r) {
        if s > 'z' {
            return rune(s - 26)
        } else if s < 'a' {
            return rune(s + 26)
        }
    } else if unicode.IsUpper(r) {
        if s > 'Z' {
            return rune(s - 26)
        } else if s < 'A' {
            return rune(s + 26)
        }
    }
    return rune(s)
}

func getReversed(str string) (reversed string) {
    for _, s := range str {
        reversed = string(s) + reversed
    }
    return reversed
}