package kata

import (
	"testing"
)

type testCase struct {
	a 			int
	b			int
	c 			int
	expected 	float32
}

var testCases = []testCase{
	{3, 4, 5, 6.0},
	{3, 5, 4, 6.0},
	{4, 3, 5, 6.0},
	{4, 5, 3, 6.0},
	{5, 3, 4, 6.0},
	{5, 4, 3, 6.0},
	{11, 13, 7, 38.49},
}

func TestCountRedBeads(t *testing.T) {
	for _, testCase := range testCases {
		if Heron(testCase.a, testCase.b, testCase.c) != testCase.expected {
			t.Errorf("%f should be %f\n", Heron(testCase.a, testCase.b, testCase.c), testCase.expected)
		}
	}
}
