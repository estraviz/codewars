// Strong Number (Special Numbers Series #2)
package kata

import (
	"strconv"
)

func Strong(n int) string {
    numStr := strconv.Itoa(n)
    acc := 0
    for _, digit := range numStr {
        value, _ := strconv.Atoi(string(digit))
        acc += factorial(value)
    }
    if acc == n {
        return "STRONG!!!!"
    }
    return "Not Strong !!"
}

func factorial(x int) int {
    if x > 1 {
        return x * factorial(x - 1)
    } else {
        return 1
    }
}
