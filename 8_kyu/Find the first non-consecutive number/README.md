# Find the first non-consecutive number

Your task is to find the first element of an array that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the array.

E.g. If we have an array `[1,2,3,4,6,7,8]` then `1` then `2` then `3` then `4` are all consecutive but `6` is not, so that's the first non-consecutive number.

If the whole array is consecutive then return `null`[^bignote].

The array will always have at least `2` elements[^2] and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

If you like this Kata, maybe try this one next: [https://www.codewars.com/kata/represent-array-of-numbers-as-ranges](https://www.codewars.com/kata/represent-array-of-numbers-as-ranges)

[^2]: Can you write a solution that will return null for both `[]` and `[ x ]` though? (This is an empty array and one with a single number and is not tested for, but you can write your own example test. )
[^bignote]:
    - Swift, Ruby and Crystal: `nil`
    - Haskell: `Nothing`
    - Python, Rust, Scala: `None`
    - Julia: `nothing`
    - Nim: `none(int)` (See [options](https://nim-lang.org/docs/options.html))
