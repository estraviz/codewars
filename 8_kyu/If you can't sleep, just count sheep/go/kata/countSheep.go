package kata

import "fmt"

func countSheep(num int) string {
	murmur := ""

	for i := 1; i <= num; i++ {
		murmur += fmt.Sprint(i) + " sheep..."
	}

	return murmur
}
