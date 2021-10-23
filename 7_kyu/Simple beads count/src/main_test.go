package main

import (
	"testing"
)

type testCase struct {
	num 		int
	expected	int
}

var testCases = []testCase{
	{0, 0},
	{1, 0},
	{3, 4},
	{5, 8},
}

func TestCountRedBeads(t *testing.T) {
	for _, testCase := range testCases {
		if CountRedBeads(testCase.num) != testCase.expected {
			t.Errorf("%d should be %d\n", testCase.num, testCase.expected)
		}
	}
}

