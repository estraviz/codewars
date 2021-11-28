package kata

import (
	"testing"
)

type testCase struct {
	s 			string
	n			int
	expected 	string
}

var testCases = []testCase{
	{"I LOVE YOU!!!", 1, "!!!vPz fWpM J"},
	{"I LOVE YOU!!!", 0, "!!!uOy eVoL I"},
	{"AAABBCCY", 1, "zDdCcBbB"},
	{"MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2, "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO"},
	{"OSHX  1 9XO 8!LRJJWQBL4QA11!Z2Z#X6!L36T! KDL", 13, "yQx !G36y!3K#M7M!88Nd5yOdJwWeY!1 Bk0 8  kUfB"},
	{"BORN IN 2015!", 1, "!4897 Oj oSpC"},
}

func TestPlayPass(t *testing.T) {
	for _, testCase := range testCases {
		if PlayPass(testCase.s, testCase.n) != testCase.expected {
			t.Errorf("%s should be %s\n", PlayPass(testCase.s, testCase.n), testCase.expected)
		}
	}
}
