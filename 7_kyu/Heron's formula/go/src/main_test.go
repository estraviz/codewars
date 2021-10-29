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
}

func TestCountRedBeads(t *testing.T) {
	for _, testCase := range testCases {
		if Heron(testCase.a, testCase.b, testCase.c) != testCase.expected {
			t.Errorf("%f should be %f\n", Heron(testCase.a, testCase.b, testCase.c), testCase.expected)
		}
	}
}
