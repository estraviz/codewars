package kata

func Quadratic(x1, x2 int) [3]int {
	a := 1
	b := -(x1 + x2)
	c := x1 * x2
	return [3]int{a, b, c}
}
