package kata

import (
	"testing"
)

type testCase struct {
	n 			int
	expected 	string
}

var testCases = []testCase{
	{0, "0"},
	{1, "01"},
	{2, "010"},
	{3, "01001"},
	{5, "0100101001001"},
}

func TestSimpleFibonacciStrings(t *testing.T) {
	for _, testCase := range testCases {
		if Solve(testCase.n) != testCase.expected {
			t.Errorf("%s should be %s\n", Solve(testCase.n), testCase.expected)
		}
	}
}
