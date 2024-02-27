package kata

import "testing"

type QuarterOfTest struct {
	month    int
	expected int
}

var QuarterOfTests = []QuarterOfTest{
	{3, 1},
	{8, 3},
	{11, 4},
}

func TestQuarterOf(t *testing.T) {

	for _, test := range QuarterOfTests {
		if got := QuarterOf(test.month); got != test.expected {
			t.Errorf("QuarterOf(%d) = %v; want %v", test.month, got, test.expected)
		}
	}
}
