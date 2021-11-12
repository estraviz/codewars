// Looking for a benefactor
package kata

func NewAvg(arr []float64, navg float64) int64 {
    var sum float64
    for _, x := range arr {
        sum += x
    }
    newAvg := int64(float64(len(arr) + 1) * navg - sum + 0.5)
    if newAvg < 0 {
        return -1
    }
    return newAvg
}
