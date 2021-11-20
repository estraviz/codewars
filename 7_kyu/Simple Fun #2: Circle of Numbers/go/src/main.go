// Simple Fun #2: Circle of Numbers
package kata

func CircleOfNumbers(n int, firstNumber int) int {
    return (n / 2 + firstNumber) % n
}
