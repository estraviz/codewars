// Alphabet symmetry
package kata

import "unicode"

func solve(slice []string) []int {
  var results []int
  for _, word := range slice {
    count := 0
    for i, r := range word {
      if i + 1 == int(unicode.ToUpper(r)) - 64 {
        count++
      }
    }
    results = append(results, count)
  }
  return results
}