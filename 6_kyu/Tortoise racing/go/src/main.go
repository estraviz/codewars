// Tortoise racing
package kata

func Race(v1, v2, g int) [3]int {
    if v1 >= v2 {
        return [3]int{-1, -1, -1}
    }

    t_sec := 3600 * g / (v2 - v1)

    return [3]int{
      t_sec / 3600,
      (t_sec % 3600) / 60,
      t_sec % 60,
    }
}