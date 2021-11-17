// Sum of Digits / Digital Root
package kata

func DigitalRoot(n int) int {
  var sum, rem int
  for n > 9 {
    sum, rem = 0, 0
    for n != 0 {
      rem = n % 10
      sum += rem
      n /= 10
    }
    n = sum
  }
  return n
}
