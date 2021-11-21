// Simple Fun #3: Late Ride
package kata

import (
	"strconv"
)

func LateRide(n int) int {
    var sum int
    for _, digit := range strconv.Itoa(n / 60) + strconv.Itoa(n % 60) {
        num, err := strconv.Atoi(string(digit))
        if err != nil {
            panic(err)
        } else {
            sum += num
        }
    }
    return sum
}