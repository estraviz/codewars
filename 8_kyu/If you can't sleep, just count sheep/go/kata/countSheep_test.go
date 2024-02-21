package kata

import "testing"

type countSheepTest struct {
	input    int
	expected string
}

var countSheepTests = []countSheepTest{
	{2, "1 sheep...2 sheep..."},
	{0, ""},
	{1, "1 sheep..."},
}

func TestCountSheep(t *testing.T) {

	for _, test := range countSheepTests {
		if got := countSheep(test.input); got != test.expected {
			t.Errorf("countSheep(%d) = %v; want %v", test.input, got, test.expected)
		}
	}
}
