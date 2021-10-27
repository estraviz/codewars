package kata

import (
	"testing"
)

type testCase struct {
	word 		string
	expected 	string
}

var testCases = []testCase{
	{"knife", "The Knife"},
	{"tart", "Tartart"},
	{"sandles", "Sandlesandles"},
	{"bed", "The Bed"},
}

func TestBandNameGenerator(t *testing.T) {
	for _, testCase := range testCases {
		if bandNameGenerator(testCase.word) != testCase.expected {
			t.Errorf("%s should be %s\n", bandNameGenerator(testCase.word), testCase.expected)
		}
	}
}
