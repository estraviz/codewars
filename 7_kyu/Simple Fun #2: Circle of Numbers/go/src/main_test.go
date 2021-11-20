package kata

import (
	"testing"
)

type testCase struct {
	n 			int
	firstNumber int
	expected 	int
}

var testCases = []testCase{
	{10, 2, 7},
	{10, 7, 2},
	{4, 1, 3},
	{6, 3, 0},
	{20, 0, 10},
}

func TestCircleOfNumbers(t *testing.T) {
	for _, testCase := range testCases {
		if CircleOfNumbers(testCase.n, testCase.firstNumber) != testCase.expected {
			t.Errorf("%d should be %d\n", CircleOfNumbers(testCase.n, testCase.firstNumber), testCase.expected)
		}
	}
}
