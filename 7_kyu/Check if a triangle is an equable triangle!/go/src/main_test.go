package kata

import (
	"testing"
)

type testCase struct {
	a 			int
	b			int
	c 			int
	expected 	bool
}

var testCases = []testCase{
	{5, 12, 13, true},
	{2, 3, 4, false},
	{6, 8, 10, true},
	{7, 15, 20, true},
	{17, 17, 30, false},
	{7, 10, 12, false},
	{6, 11, 12, false},
	{25, 25, 45, false},
	{13, 37, 30, false},
	{6, 25, 29, true},
	{10, 11, 18, false},
	{73, 9, 80, false},
	{12, 35, 37, false},
	{120, 109, 13, false},
	{9, 10, 17, true},
}

func TestCountRedBeads(t *testing.T) {
	for _, testCase := range testCases {
		if EquableTriangle(testCase.a, testCase.b, testCase.c) != testCase.expected {
			t.Errorf("%v should be %v\n", EquableTriangle(testCase.a, testCase.b, testCase.c), testCase.expected)
		}
	}
}
