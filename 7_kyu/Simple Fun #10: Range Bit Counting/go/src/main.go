// Simple Fun #10: Range Bit Counting
package kata

import (
	"strconv"
)

func RangeBitCount(a,b int) int {
    var sum int
    x := a
    for x <= b {
        xStr := strconv.FormatInt(int64(x), 2)
        for _, r := range xStr {
            digit, _ := strconv.Atoi(string(r))
            sum += digit
        }
        x += 1
    }
    return sum
}
