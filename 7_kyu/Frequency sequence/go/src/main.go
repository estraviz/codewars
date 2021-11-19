// Frequency sequence
package kata

import "strconv"

func FreqSeq(str string, sep string) string {
    var seq string

    counter := countLetters(str)

    for i, c := range str {
        seq += strconv.Itoa(counter[string(c)])
        if i != len(str) - 1 {
            seq += sep
        }
    }

    return seq
}

func countLetters(str string) map[string]int {
    counter := make(map[string]int)

    for _, c := range str {
        counter[string(c)]++
    }
    return counter
}
