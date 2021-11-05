package kata

import (
	"testing"
)

type testCase struct {
	a, b 		int
	expected 	int
}

var testCases = []testCase{
	{2, 7, 11},
	{0, 1, 1},
	{4, 4, 1},
}

func TestSingleStringCharacters(t *testing.T) {
	for _, testCase := range testCases {
		if RangeBitCount(testCase.a, testCase.b) != testCase.expected {
			t.Errorf("%d should be %d\n", RangeBitCount(testCase.a, testCase.b), testCase.expected)
		}
	}
}
