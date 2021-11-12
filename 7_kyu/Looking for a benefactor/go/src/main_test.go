package kata

import (
	"testing"
)

type testCase struct {
	arr 		[]float64
	navg		float64
	expected 	int64
}

var testCases = []testCase{
	{[]float64{14.0, 30.0, 5.0, 7.0, 9.0, 11.0, 16.0}, 90, 628},
	{[]float64{14, 30, 5, 7, 9, 11, 15}, 92, 645},
	{[]float64{1400.25, 30000.76, 5.56, 7, 9, 11, 15.48, 120.98}, 2000, -1},
	{[]float64{1400.25, 30000.76, 5.56, 7, 9, 11, 15.48, 120.98}, 10000, 58430},
	{[]float64{1400.25, 30000.76, 5.56, 7, 9, 11, 15.48, 120.98}, 5800, 20630},
	{[]float64{1400.25, 30000.76, 5.56, 7, 9, 11, 15.48, 120.98}, 4800, 11630},
	{[]float64{}, 90, 90},
	{[]float64{14000.25, 300.76, 50.56, 70, 90, 11, 150.48, 1200.98}, 4800, 27326},
	{[]float64{14.25, 30.76, 5.56, 7, 9, 11, 15.48, 12.987}, 5, -1},
}

func TestNewAvg(t *testing.T) {
	for _, testCase := range testCases {
		if NewAvg(testCase.arr, testCase.navg) != testCase.expected {
			t.Errorf("%d should be %d\n", NewAvg(testCase.arr, testCase.navg), testCase.expected)
		}
	}
}
