// Simple fibonacci strings
package kata

func Solve(n int) string {
  var fk0, fk1 string = "0", "1"
  var sum string

  for k := 0; k < n + 1; k++ {
    sum += fk0
    fk0, fk1 = fk1, sum
  }
  return sum
}
