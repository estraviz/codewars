// Heron's formula
package kata

import (
	"math"
)

func Heron(a, b, c int) (area float32) {
    s := SemiPerimeter(a, b, c)
    radical := float64(s * (s - float32(a)) * (s - float32(b)) * (s - float32(c)))
    return float32(math.Sqrt(radical))
}

func SemiPerimeter(a, b, c int) float32 {
    return float32(a + b + c) / 2
}
