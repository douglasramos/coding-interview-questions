# Python Tips

### For Loop with index:

```python
items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)

# or use range
# range(start, end not inclusive, step)
# range(end not inclusive) -> start=0 step=1
# range(start, end not inclusive) -> step=1
for index in range(len(item)):
    print(index, items[index])
```

### Array/Lists:

```python
append()	# Adds an element at the end of the list
clear()	    # Removes all the elements from the list
copy()	    # Returns a copy of the list
lst[:]      # Returns a copy of the list
count()	    # Returns the number of elements with the specified value
extend()	# Add the elements of a list (or any iterable), to the end of the current list
index()	    # Returns the index of the first element with the specified value
insert()	# Adds an element at the specified position
pop()	    # Removes and returns the element at the specified position. Without arguments removes the last one
[-1]        # get the last value
remove()	# Removes the first item with the specified value. Return None
reverse()	# Reverses the order of the list. Retuns None
sort()	    # Sorts the list. Returns None

# sort the list by length of values:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

# sort the list in reverse order:
cars.sort(reverse=True)

# sort keeping original array
newArr = sorted(cars, key=myFunc, reverse=False)

# you can get the max number in an array by doing
max(arr) # arr needs to be a non-empty array
```

### Range  

In python3, range(n) will return an iterator(without creating the whole n-length list), so the space complexity is O(1).

(0 to N)
```python
range(0, N+1)
```

(N to 0)
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

PS.: Slice generates another list. Changes to the new list don't modify the original one

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

One can use any immutable data struct as key of dict.
Eg. numbers, strings and tuples.
PS. you can't use objects or lists, because they are mutable. If you want to use a list, do `tuple(myList)`

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

## Heaps

https://www.educative.io/answers/min-heap-vs-max-heap

https://stackoverflow.com/questions/39095000/if-siftdown-is-better-than-siftup-why-do-we-have-it

insertion and extraction of the minimum element in O(log n) time, where n is the size of the heap.


```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self, i):
        return len(heap)

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def sift_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        min_value = self.heap[0]
        last_value = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_value
            self.heapify_down(0)
        return min_value

    def sift_down(self, i):
        while i < self.size():
            min_index = i
            left = self.left_child(i)
            right = self.right_child(i)
            if left < self.size() and self.heap[left] < self.heap[min_index]:
                min_index = left
            if right < self.size() and self.heap[right] < self.heap[min_index]:
                min_index = right
            if i != min_index:
                self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
                i = min_index
            else:
                break

    def build_heap(self, arr):
        self.heap = arr[:]
        n = self.size()
        start = self.parent(n - 1)
        for i in range(start, -1, -1):
            self.siftDown(i)
```

## Binary Seach Tree

To cut the parent node thal will split the list in the middle use `len(n) // 2` to get the index of the parent  node
or `endIdx + startIdx // 2`