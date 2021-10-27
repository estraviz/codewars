package main

import (
	"testing"
)

type testCase struct {
	st 			string
	arr			[]int
	expected 	string
}

var testCases = []testCase{
	{"abcdef", []int {1, 2, 5}, "aBCdeF"},
	{"abcdef", []int {1, 2, 5, 100}, "aBCdeF"},
	{"codewars", []int {1, 3, 5, 50}, "cOdEwArs"},
	{"abracadabra", []int {2, 6, 9, 10}, "abRacaDabRA"},
	{"codewarriors",[]int {5}, "codewArriors"},
	{"indexinglessons",[]int {0}, "Indexinglessons"},
}

func TestCountRedBeads(t *testing.T) {
	for _, testCase := range testCases {
		if Capitalize(testCase.st, testCase.arr) != testCase.expected {
			t.Errorf("%s should be %s\n", Capitalize(testCase.st, testCase.arr), testCase.expected)
		}
	}
}
