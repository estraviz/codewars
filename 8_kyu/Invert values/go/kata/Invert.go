package kata

func Invert(arr []int) []int {
    if arr == nil {
        return nil
    }

	result := []int{}

	for _, num := range arr {
		result = append(result, -1*num)
	}

	return result
}
