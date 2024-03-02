package kata

import (
	"strconv"
	"strings"
)

func Points(games []string) int {
  points := 0

  for _, score := range games {
    goals := strings.Split(score, ":")
    homeScore, _ := strconv.Atoi(goals[0])
    awayScore, _ := strconv.Atoi(goals[1])

    switch {
    case homeScore > awayScore:
      points += 3
    case homeScore == awayScore:
      points += 1
    }
  }

  return points
}