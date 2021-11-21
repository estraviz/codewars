package kata

import (
	"testing"
)

type testCase struct {
	n 			int
	expected 	int
}

var testCases = []testCase{
	{240, 4},
	{808, 14},
	{1439, 19},
	{0, 0},
	{23, 5},
	{8, 8},
}

func TestLateRide(t *testing.T) {
	for _, testCase := range testCases {
		if LateRide(testCase.n) != testCase.expected {
			t.Errorf("%d should be %d\n", LateRide(testCase.n), testCase.expected)
		}
	}
}
