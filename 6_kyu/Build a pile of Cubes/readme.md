# Build a pile of Cubes

## Description

Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n<sup>3</sup>, the cube above will have volume of (n-1)<sup>3</sup> and so on until the top which will have a volume of 1<sup>3</sup>.

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb `(find_nb, find-nb, findNb)` will be an integer m and you have to return the integer n such as n<sup>3</sup> + (n-1)<sup>3</sup> + ... + 1<sup>3</sup> = m if such a n exists or -1 if there is no such n.

## Examples

```python
findNb(1071225) --> 45
findNb(91716553919377) --> -1
```
