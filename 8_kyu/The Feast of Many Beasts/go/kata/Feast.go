package kata

func Feast(beast string, dish string) bool {
	return beast[0] == dish[0] && beast[len(beast)-1:] == dish[len(dish)-1:]
}
