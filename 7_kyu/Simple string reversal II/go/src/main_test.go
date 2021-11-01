package kata

import (
	"testing"
)

type testCase struct {
	s 			string
	a, b 		int
	expected 	string
}

var testCases = []testCase{
	{"codewars",1,5,"cawedors"},
	{"codingIsFun",2,100, "conuFsIgnid"},
	{"FunctionalProgramming", 2, 15,"FuargorPlanoitcnmming"},
	{"abcefghijklmnopqrstuvwxyz",0,20, "vutsrqponmlkjihgfecbawxyz"},
	{"abcefghijklmnopqrstuvwxyz",5,20, "abcefvutsrqponmlkjihgwxyz"},
}

func TestSingleStringReversal(t *testing.T) {
	for _, testCase := range testCases {
		if Solve(testCase.s, testCase.a, testCase.b) != testCase.expected {
			t.Errorf("%v should be %v\n", Solve(testCase.s, testCase.a, testCase.b), testCase.expected)
		}
	}
}
