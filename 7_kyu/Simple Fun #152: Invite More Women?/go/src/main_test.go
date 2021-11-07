package kata

import (
	"testing"
)

type testCase struct {
	L 			[]int
	expected 	bool
}

var testCases = []testCase{
	{[]int{1, -1, 1}, true},
	{[]int{1, 1, 1}, true},
	{[]int{-1, -1, -1}, false},
	{[]int{1, -1}, false},
}

func TestSingleStringCharacters(t *testing.T) {
	for _, testCase := range testCases {
		if inviteMoreWomen(testCase.L) != testCase.expected {
			t.Errorf("%v should be %v\n", inviteMoreWomen(testCase.L), testCase.expected)
		}
	}
}
