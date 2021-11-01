// Simple string reversal II
package kata

func Solve(s string, a, b int) string {

    if b < len(s) {
        return s[:a] + reverse(s[a:b+1]) + s[b+1:]
    } else {
        return s[:a] + reverse(s[a:len(s)])
    }
}

func reverse(s string) string {

    var res []rune
    r := []rune(s)

    for i := len(r) - 1; i >= 0; i-- {
        res = append(res, r[i])
    }

    return string(res)
}
