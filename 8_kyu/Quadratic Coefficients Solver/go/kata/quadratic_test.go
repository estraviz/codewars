package kata

import "testing"

type quadraticTest struct {
	x1       int
	x2       int
	expected [3]int
}

var quadraticTests = []quadraticTest{
	{0, 1, [3]int{1, -1, 0}},
	{4, 9, [3]int{1, -13, 36}},
	{2, 6, [3]int{1, -8, 12}},
	{-5, -4, [3]int{1, 9, 20}},
}

func TestQuadratic(t *testing.T) {

	for _, test := range quadraticTests {
		if got := Quadratic(test.x1, test.x2); got != test.expected {
			t.Errorf("Quadratic(%d, %d) = %v; want %v", test.x1, test.x2, got, test.expected)
		}
	}
}
