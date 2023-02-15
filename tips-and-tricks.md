# Tips and tricks

# trading time complexity for space complexity

Sometimes you will need to increase the space complexity so you can reduce the time complexity. In such cases you generally want to use an auxiliary data scruture (therefore increasing the space complexity) that will help you reduce one or more loops in the algorithm. This data structure is generally a **hashmap**, since its lookup time is O(1).

### Transforming an array into a hashmap (javascript):

Object:

```javascript
// how you will build the hashmap will depend on the use case
arr.reduce((map, arrValue, index) => {...map, [arrValue]: index}, {});
```

Map:

```javascript
arr.reduce((map, arrValue, index) => map.set(arrValue, index), new Map());
```

[Map vs Objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)

`TL;DR:` Both provide equivalent solutions for most cases, use Map when you want a proper hashmap that allows any type of keys. You can use Objects for keys of string type. With objects, you will get a simpler api to use


### Transforming an array into a hashmap (clojure):
```clojure
(->> arr
     (map-indexed vector)
     (reduce #(assoc %1 (first %2) (second %2)) {})) ;; or (into {})

;; if you don't need the index, you can simply go with
(reduce some-fn {} arr)
```