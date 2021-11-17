package kata

import (
	"testing"
)

type testCase struct {
	n 			int
	expected 	int
}

var testCases = []testCase{
	{16, 7},
	{195, 6},
	{992, 2},
	{167346, 9},
	{0, 0},
}

func TestDigitalRoot(t *testing.T) {
	for _, testCase := range testCases {
		if DigitalRoot(testCase.n) != testCase.expected {
			t.Errorf("%v should be %d\n", DigitalRoot(testCase.n), testCase.expected)
		}
	}
}
