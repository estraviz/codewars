// Simple beads count
package main

func CountRedBeads(n int) int {
  if n >= 2 {
    return (n - 1) * 2
  }
  return 0
}
