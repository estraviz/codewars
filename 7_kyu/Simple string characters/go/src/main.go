// Simple string characters
package kata

import (
	"unicode"
)

func Solve(s string) []int {
	var uppercase int
    var lowercase int
    var number int
    var special int
    for _, c := range s {
        if unicode.IsUpper(c) {
            uppercase++
        } else if unicode.IsLower(c) {
            lowercase++
        } else if unicode.IsNumber(c) {
            number++
        } else {
            special++
        }
    }
    return []int {uppercase, lowercase, number, special}
}
