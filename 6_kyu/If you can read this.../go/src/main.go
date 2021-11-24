// If you can read this...
package kata

import (
	"strings"
	"unicode"
)

func ToNato(words string) string {
  var output string

  for _, ch := range words {
    if !unicode.IsSpace(ch) {
      if unicode.IsLetter(ch) {
        output += getNatoWord(ch) + " "
      } else {
        output += string(ch)
      }
    }
  }
  return strings.TrimSpace(output)
}

func getNatoWord(ch rune) string {
  nato := []string{"Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot","Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"}

  for _, w := range nato {
    if strings.HasPrefix(w, strings.ToUpper(string(ch))) {
      return w
    }
  }
  panic("Parse error!")
}