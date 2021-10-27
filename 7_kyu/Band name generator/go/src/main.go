// Band name generator
package kata

import (
	"strings"
)

func bandNameGenerator(word string) string {
    if strings.HasPrefix(word, string(word[0])) == strings.HasSuffix(word, string(word[0])) {
        return strings.Title(word) + word[1:]
    }
    return "The " + strings.Title(word)
}
