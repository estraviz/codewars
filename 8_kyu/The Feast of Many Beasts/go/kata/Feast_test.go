package kata

import "testing"

type feastTest struct {
	beast    string
	dish     string
	expected bool
}

var feastTests = []feastTest{
	{"great blue heron", "garlic naan", true},
	{"chickadee", "chocolate cake", true},
	{"brown bear", "bear claw", false},
}

func TestFeast(t *testing.T) {

	for _, test := range feastTests {
		if got := Feast(test.beast, test.dish); got != test.expected {
			t.Errorf("Feast(%s, %s) = %v; want %v", test.beast, test.dish, got, test.expected)
		}
	}
}
