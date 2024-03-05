package kata

import (
	"reflect"
	"testing"
)

type InvertTest struct {
	arr      []int
	expected []int
}

var InvertTests = []InvertTest{
	{[]int{1, 2, 3, 4, 5}, []int{-1, -2, -3, -4, -5}},
	{[]int{1, -2, 3, -4, 5}, []int{-1, 2, -3, 4, -5}},
	{nil, nil},
	{[]int{0}, []int{0}},
}

func EqualSlicesInt(a, b[] int)  bool {
	if a == nil && b == nil {
		return true
	}
	return reflect.DeepEqual(a, b)
}

func TestInvert(t *testing.T) {

	for _, test := range InvertTests {
		if got := Invert(test.arr); !EqualSlicesInt(got, test.expected) {
			t.Errorf("Invert(%v) = %v; want %v", test.arr, got, test.expected)
		}
	}
}
