// Check if a triangle is an equable triangle!
package kata

import (
	"math"
)

func EquableTriangle(a, b, c int) bool {
    return Area(a, b, c) == Perimeter(a, b, c)
}

func SemiPerimeter(a, b, c int) float64 {
    return float64(a + b + c) / 2
}

func Area(a, b, c int) float64 {
    s := SemiPerimeter(a, b, c)
    return math.Sqrt(s * (s - float64(a)) * (s - float64(b)) * (s - float64(c)))
}

func Perimeter(a, b, c int) float64 {
    return float64(a + b + c)
}
