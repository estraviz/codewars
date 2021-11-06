package kata

import (
	"testing"
)

type testCase1 struct {
	player1, player2 	NBAPlayer
	expected 			float64
}

var testCases1 = []testCase1{
	{NBAPlayer{ Team: "76ers", Ppg: 11.2 }, NBAPlayer{ Team: "bulls", Ppg: 20.2 }, 31.4},
}

func TestIversonJordanPpg(t *testing.T) {
	for _, testCase1 := range testCases1 {
		if SumPpg(testCase1.player1, testCase1.player2) != testCase1.expected {
			t.Errorf("%f should be %f\n", SumPpg(testCase1.player1, testCase1.player2), testCase1.expected)
		}
	}
}

type testCase2 struct {
	player1, player2 	NBAPlayer
	expected 			float64
}

var testCases2 = []testCase2{
	{NBAPlayer{ Team: "p1_team", Ppg: 20.2 }, NBAPlayer{ Team: "p2_team", Ppg: 2.6 }, 22.8},
	{NBAPlayer{ Team: "p3_team", Ppg: 2023.2 }, NBAPlayer{ Team: "p1_team", Ppg: 20.2 }, 2043.4},
	{NBAPlayer{ Team: "p3_team", Ppg: 2023.2 }, NBAPlayer{ Team: "p4_team", Ppg: 0 }, 2023.2},
	{NBAPlayer{ Team: "p4_team", Ppg: 0 }, NBAPlayer{ Team: "p5_team", Ppg: -5.8 }, -5.8},
}

func TestStandard(t *testing.T) {
	for _, testCase2 := range testCases2 {
		if SumPpg(testCase2.player1, testCase2.player2) != testCase2.expected {
			t.Errorf("%f should be %f\n", SumPpg(testCase2.player1, testCase2.player2), testCase2.expected)
		}
	}
}

