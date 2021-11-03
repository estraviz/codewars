package kata

import (
	"testing"
)

type testCase struct {
	n 			int
	expected 	string
}

var testCases = []testCase{
	{1, "STRONG!!!!"},
	{2, "STRONG!!!!"},
	{145, "STRONG!!!!"},
	{7, "Not Strong !!"},
	{93, "Not Strong !!"},
	{185, "Not Strong !!"},
}

func TestStrongNumbers(t *testing.T) {
	for _, testCase := range testCases {
		if Strong(testCase.n) != testCase.expected {
			t.Errorf("%s should be %s\n", Strong(testCase.n), testCase.expected)
		}
	}
}
