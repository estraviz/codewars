library(testthat)

setwd(system("pwd", intern = T) )
source("stanton_measure.R")

test_that("Sample Test", {
  expect_equal(stanton_measure(c(1, 4, 3, 2, 1, 2, 3, 2)), 3)
})

test_that("Random Tests", {
  replicate(100, { # Do this 100 times
    x = sample(2:100, 1) # each time pick a number x, equal to the number of 1s
    exp = sample(10, 1) # pick a number of times to have x in the array
    o = sample(100, sample(10:30, 1), replace = TRUE) # create a random integer vector
    o = o[o!=1 & o!=x] # remove the 1s and xs from that vector
    arr = sample(c(rep(1, x), rep(x, exp), o)) # put together the 1s, xs, and other
    expect_equal(stanton_measure(arr), exp) # is the stanton measure the same as the number of xs?
  })
})