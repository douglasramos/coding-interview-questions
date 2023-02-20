# Python Tips

### For Loop with index:

```python
items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)

# or use range(start, end not inclusive, step=1)
for index in range(0, len(item)):
    print(index, items[index])
```

### Array/Lists:

```python
append()	# Adds an element at the end of the list
clear()	    # Removes all the elements from the list
copy()	    # Returns a copy of the list
count()	    # Returns the number of elements with the specified value
extend()	# Add the elements of a list (or any iterable), to the end of the current list
index()	    # Returns the index of the first element with the specified value
insert()	# Adds an element at the specified position
pop()	    # Removes and returns the element at the specified position. Withou arguments removes the last one
[-1]       # get the last value
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

### Range  (0 to N)

```python
range(0, N+1)
```

### Range (N to 0)

```python
range(N, -1, -1)
```

### Strings

```python

# sort (alphabetically)
sorted_string = ''.join(sorted("string"))

# reverse
reversed_string = "string"[::-1]
```

### Slice [start:end non inclusve:step]

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

### Dictionaries / Hashmaps

```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car.items()        # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["year"]        # get value of key | throws error
car.get("year")    # get value of key | don't throw error
car["year"] = 2020 # set new value for new or old key 
car.keys()         # list of keys
car.values()       # list of values
car.pop("year")    # remove key/value
car.popitem()      # remove last inserted key/value
if "year" in car   # predicate to check key existance

####### Loop #######

# keys
for k in car:
  print(k)

for k in car.keys():
  print(k)

# values
for v in car.values():
  print(v)

# keys and values
for k, v in car.items():
  print(k, v)
```

### List to Dict

```python
lst = [1, 2, 3]
res_dct = {lst[i]: i*10 for i in range(0, len(lst))}


lst = ['a', 1, 'b', 2]
it = iter(lst)
res_dct = dict(zip(it, it)) # {'a': 1, 'b': 2}
```

### Ternary Operator & List comprenhesion

```python
# use to define variables' value
lst = [1, 2, 3] if True else [4, 5, 6] # [1, 2, 3]

# use in loops
for item in range(0, 3) if False else range(3, 6):
  print(item) 

# use in list comprenshion
res_dct = {lst[i]: i*10 for i in range(0, len(lst)) if i % 2 == 0 }
```
