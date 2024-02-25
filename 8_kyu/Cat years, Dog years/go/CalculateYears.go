package kata

const (
	CatYearsFirstYear                = 15
	CatYearsIncrementSecondYear      = 9
	CatYearsIncrementAfterSecondYear = 4
	DogYearsFirstYear                = 15
	DogYearsIncrementSecondYear      = 9
	DogYearsIncrementAfterSecondYear = 5
)

func CalculateYears(years int) (result [3]int) {
	result[0] = years

	switch {
	case years == 1:
		result[1] = CatYearsFirstYear
		result[2] = DogYearsFirstYear
	case years == 2:
		result[1] = CatYearsFirstYear + CatYearsIncrementSecondYear
		result[2] = DogYearsFirstYear + DogYearsIncrementSecondYear
	case years > 2:
		result[1] = CatYearsFirstYear + CatYearsIncrementSecondYear + CatYearsIncrementAfterSecondYear*(years-2)
		result[2] = DogYearsFirstYear + DogYearsIncrementSecondYear + DogYearsIncrementAfterSecondYear*(years-2)
	}

	return result
}
