package kata

import (
	"testing"
)

type testCase struct {
	words 		string
	expected 	string
}

var testCases = []testCase{
	{"If you can read", "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta"},
	{"Did not see that coming", "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf"},
	{"go for it!", "Golf Oscar Foxtrot Oscar Romeo India Tango !"},
}

func TestIfYouCanReadThis(t *testing.T) {
	for _, testCase := range testCases {
		if ToNato(testCase.words) != testCase.expected {
			t.Errorf("%s should be %s\n", ToNato(testCase.words), testCase.expected)
		}
	}
}
