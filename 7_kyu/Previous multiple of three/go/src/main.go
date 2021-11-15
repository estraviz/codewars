// Previous multiple of three
package kata

import (
	"strconv"
)

func PrevMultOfThree(n int) interface{} {
  // write your code here
  // your function should return an int or a nil
  var nStr string
  for n > 9 {
    if isMultipleOfThree(n) {
      return n
    } else {
      nStr = strconv.Itoa(n)
      n, _ = strconv.Atoi(nStr[:len(nStr)-1])
    }
  }
  if isMultipleOfThree(n) {
    return n
  }
  return nil
}

func isMultipleOfThree(n int) bool {
  return n % 3 == 0
}
