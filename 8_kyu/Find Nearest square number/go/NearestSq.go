package kata

import "math"

func NearestSq(n int) int {
	sqrt := math.Sqrt(float64(n))

	return int(math.Pow(math.Round(sqrt), 2))
}
