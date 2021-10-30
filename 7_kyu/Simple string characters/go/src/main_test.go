package kata

import (
	"reflect"
	"testing"
)

type testCase struct {
	s 			string
	expected 	[]int
}

var testCases = []testCase{
	{"Codewars@codewars123.com", []int{1,18,3,2}},
	{"bgA5<1d-tOwUZTS8yQ", []int{7,6,3,2}},
	{"P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H", []int{9,9,6,9}},
	{"RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD", []int{15,8,6,9}},
	{"$Cnl)Sr<7bBW-&qLHI!mY41ODe", []int{10,7,3,6}},
}

func TestSingleStringCharacters(t *testing.T) {
	for _, testCase := range testCases {
		if !reflect.DeepEqual(Solve(testCase.s), testCase.expected) {
			t.Errorf("%v should be %v\n", Solve(testCase.s), testCase.expected)
		}
	}
}
