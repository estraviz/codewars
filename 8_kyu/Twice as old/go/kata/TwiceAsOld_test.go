package kata

import "testing"

type twiceAsOldTest struct {
	x1       int
	x2       int
	expected int
}

var twiceAsOldTests = []twiceAsOldTest{
	{36, 7, 22},
	{55, 30, 5},
	{42, 21, 0},
	{22, 1, 20},
	{29, 0, 29},
}

func TestTwiceAsOld(t *testing.T) {

	for _, test := range twiceAsOldTests {
		if got := TwiceAsOld(test.x1, test.x2); got != test.expected {
			t.Errorf("TwiceAsOld(%d, %d) = %v; want %v", test.x1, test.x2, got, test.expected)
		}
	}
}
