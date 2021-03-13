# Naming Files

## Description

Naming multiple files can be a pain sometimes.

### Task

Your job here is to create a function that will take three parameters, `fmt`, `nbr` and `start`, and create an array of `nbr` elements formatted according to `frm` with the starting index `start`. `fmt` will have `<index_no>` inserted at various locations; this is where the file index number goes in each file.

### Description of edge cases

1. If `nbr` is less than or equal to 0, or not whole, return an empty array.
2. If `fmt` does not contain `'<index_no>'`, just return an array with `nbr` elements that are all equal to `fmt`.
3. If `start` is not an integer, return an empty array.

### What each parameter looks like

```python
type(frm) #=> str
  : "text_to_stay_constant_from_file_to_file <index_no>"
type(nbr) #=> int
  : number_of_files
type(start) #=> int
  : index_no_of_first_file
type(name_file(frm, nbr, start)) #=> list
```

### Some examples

```python
name_file("IMG <index_no>", 4, 1)
  #=> ["IMG 1", "IMG 2", "IMG 3", "IMG 4"])
name_file("image #<index_no>.jpg", 3, 7)
  #=> ["image #7.jpg", "image #8.jpg", "image #9.jpg"]
name_file("#<index_no> #<index_no>", 3, -2)
  #=> ["#-2 #-2", "#-1 #-1", "#0 #0"]
```
