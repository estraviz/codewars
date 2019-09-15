# Aerial Firefighting

## Description

You are an aerial firefighter (someone who drops water on fires from above in order to extinguish them).

Your goal is to work out the minimum amount of bombs you need to drop on the string in order to extinguish the fire.

The string is a 2d plane of random length consisting of two characters:

```python
String 'x' representing fire
String 'Y' representing buildings.
```

Water that you drop cannot go through buildings and therefore individual sections of fire must be addressed separately.

Your water bombs can only extinguish contiguous sections of fire up to a width designated by w.

You must return the number of waterbombs it would take to extinguish the fire in the string.

Therefore, for the following strings and w values:

```python
"xxYxx" and w=3  it would take 2 waterbombs.
"xxYxx" and w=1, it would take 4 waterbombs.
"xxxxYxYx" and w=5, it would take 3 waterbombs.
"xxxxxYxYx" and w=2, it would take 5 waterbombs.
```

## Inputs and Outpus

```python
Inputs:
'fire' = the string.

W = an integer representing the width of exinguishable contiguous section per waterbomb.

Outputs:
An integer representing the number of waterbombs it would take to extinguish all the fires in the given string.
```

Assume all strings can be extinguished. Assume all inputs are valid and that the strings will only contain the symbols x or Y.
