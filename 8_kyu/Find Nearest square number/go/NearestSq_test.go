package kata

import "testing"

type NearestSqTest struct {
	n        int
	expected int
}

var NearestSqTests = []NearestSqTest{
	{1, 1},
	{2, 1},
	{10, 9},
	{111, 121},
	{9999, 10000},
}

func TestFeast(t *testing.T) {

	for _, test := range NearestSqTests {
		if got := NearestSq(test.n); got != test.expected {
			t.Errorf("NearestSq(%d) = %v; want %v", test.n, got, test.expected)
		}
	}
}
