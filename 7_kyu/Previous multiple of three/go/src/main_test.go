package kata

import (
	"testing"
)

type testCase struct {
	n 			int
	expected 	interface{}
}

var testCases = []testCase{
	{1, nil},
	{25, nil},
	{36, 36},
	{1244, 12},
	{952406, 9},
}

func TestPrevMultOfThree(t *testing.T) {
	for _, testCase := range testCases {
		if PrevMultOfThree(testCase.n) != testCase.expected {
			t.Errorf("%v should be %v for entry parameters: %d\n", PrevMultOfThree(testCase.n), testCase.expected, testCase.n)
		}
	}
}
