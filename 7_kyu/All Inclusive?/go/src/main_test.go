package kata

import (
	"testing"
)

type testCase struct {
	strng	 	string
	arr			[]string
	expected 	bool
}

var testCases = []testCase{
	{"bsjq", []string{"bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"}, true},
	{"XjYABhR", []string{"TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"}, false},
	{"", []string{}, true},
}

func TestContainAllRots(t *testing.T) {
	for _, testCase := range testCases {
		if ContainAllRots(testCase.strng, testCase.arr) != testCase.expected {
			t.Errorf("%v should be %v for entry parameters: %s, %v\n", ContainAllRots(testCase.strng, testCase.arr), testCase.expected, testCase.strng, testCase.arr)
		}
	}
}
