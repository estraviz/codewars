package kata

import "testing"

type CalculateYearsTest struct {
	years    int
	expected [3]int
}

var CalculateYearsTests = []CalculateYearsTest{
	{1, [3]int{1, 15, 15}},
	{2, [3]int{2, 24, 24}},
	{3, [3]int{3, 28, 29}},
	{10, [3]int{10, 56, 64}},
}

func TestCalculateYears(t *testing.T) {

	for _, test := range CalculateYearsTests {
		if got := CalculateYears(test.years); got != test.expected {
			t.Errorf("Feast(%d) = %v; want %v", test.years, got, test.expected)
		}
	}
}
