package kata

import (
	"testing"
	"reflect"
)

type testCase struct {
	slice 		[]string
	expected 	[]int
}

var testCases = []testCase{
	{[]string{"abode","ABc","xyzD"}, []int{4,3,1}},
	{[]string{"abide","ABc","xyz"}, []int{4,3,0}},
	{[]string{"IAMDEFANDJKL","thedefgh","xyzDEFghijabc"}, []int{6,5,7}},
	{[]string{"encode","abc","xyzD","ABmD"}, []int{1,3,1,3}},
}

func TestAlphabetSymmetry(t *testing.T) {
	for _, testCase := range testCases {
		if !reflect.DeepEqual(solve(testCase.slice), testCase.expected) {
			t.Errorf("%v should be %v\n", solve(testCase.slice), testCase.expected)
		}
	}
}
