package kata

import (
	"testing"
)

type testCase struct {
	str 		string
	sep			string
	expected 	string
}

var testCases = []testCase{
	{"hello world", "-", "1-1-3-3-2-1-1-2-1-3-1"},
	{"19999999", ":", "1:7:7:7:7:7:7:7"},
	{"^^^**$", "x", "3x3x3x2x2x1"},
}

func TestFreqSeq(t *testing.T) {
	for _, testCase := range testCases {
		if FreqSeq(testCase.str, testCase.sep) != testCase.expected {
			t.Errorf("%s should be %s\n", FreqSeq(testCase.str, testCase.sep), testCase.expected)
		}
	}
}
