# Stanton measure

stanton_measure <- function(arr){
  n <- 0
  for (num in arr) {
    if (num == 1) {
      n <- n + 1
    }
  }
  times <- 0
  for (num in arr) {
    if (num == n) {
      times <- times + 1
    }
  }
  return (times)
}
