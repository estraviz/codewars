package kata

import (
	"testing"
)

type testCase struct {
	v1 			int
	v2			int
	g 			int
	expected 	[3]int
}

var testCases = []testCase{
	{720, 850, 70, [3]int{0, 32, 18}},
	{820, 81, 550, [3]int{-1, -1, -1}},
	{80, 91, 37, [3]int{3, 21, 49}},
	{80, 100, 40, [3]int{2, 0, 0}},
	{720, 850, 37, [3]int{0, 17, 4}},
	{720, 850, 370, [3]int{2, 50, 46}},
	{120, 850, 37, [3]int{0, 3, 2}},
	{820, 850, 550, [3]int{18, 20, 0}},
}

func TestTortoiseRacing(t *testing.T) {
	for _, testCase := range testCases {
		if Race(testCase.v1, testCase.v2, testCase.g) != testCase.expected {
			t.Errorf("%v should be %v\n", Race(testCase.v1, testCase.v2, testCase.g), testCase.expected)
		}
	}
}
