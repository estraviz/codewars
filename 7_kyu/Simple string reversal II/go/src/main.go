// Simple string reversal II
package kata

func Solve(s string, a, b int) string {
	var first, second, third []rune

    for i, c := range s {
        if i < a {
            first = append(first, c)
        } else if i >= a && i <= b {
            second = append(second, c)
        } else {
            third = append(third, c)
        }
    }

    return string(first) + string(reverse(second)) + string(third)
}

func reverse(r []rune) []rune {
    var res []rune

    for i := len(r) - 1; i >= 0; i-- {
        res = append(res, r[i])
    }

    return res
}
