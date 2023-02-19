# Python Tips

For Loop with index:

```python
items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)

# or use range(start, end not inclusive, step=1)
for index in range(0, len(item)):
    print(index, items[index])
```

Array/Lists:

```python
append()	# Adds an element at the end of the list
clear()	    # Removes all the elements from the list
copy()	    # Returns a copy of the list
count()	    # Returns the number of elements with the specified value
extend()	# Add the elements of a list (or any iterable), to the end of the current list
index()	    # Returns the index of the first element with the specified value
insert()	# Adds an element at the specified position
pop()	    # Removes and returns the element at the specified position. Withou arguments removes the last one
remove()	# Removes the first item with the specified value. Return None
reverse()	# Reverses the order of the list. Retuns None
sort()	    # Sorts the list. Returns None

# Examples:

# sort the list by length of values:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

# sort the list in reverse order:
cars.sort(reverse=True)
```

Range  (0 to N)

```python
range(0, N+1)
```

Range  (N to 0)

```python
range(N, -1, -1)
```

Strings

```python

# sort (alphabetically)
sorted_string = ''.join(sorted("string"))

# reverse
reversed_string = "string"[::-1]
```

Slice [start:end non inclusve:step]
```python 

"string"[::]    # "string"
"string"[:]     # "string"

"string"[:2]    # "st"
"string"[0:2]   # "st"
"string"[0:2:]  # "st"
"string"[0:2:1] # "st"

"string"[2:]    # "ring"
"string"[2::]   # "ring"
"string"[2::1]  # "ring"

"string"[2:-1]  # "rts"
"string"[2:-2]  # "rs"

```