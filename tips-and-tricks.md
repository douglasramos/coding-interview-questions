# Tips and tricks

# trading time complexity for space complexity

Sometimes you will need to increase the space complexity so you can reduce the time complexity. In such cases you generally want to use an auxiliary data scruture (therefore increasing the space complexity) that will help you reduce one or more loops in the algorithm. This data structure is generally a **hashmap**, since its lookup time is O(1).

## Transforming an array into a hashmap (javascript):

```javascript
// how you will build the hashmap will depend on the use case
arr.reduce((map, arrValue, index) => map[arrValue] = index, {});
```
[Map vs Objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)

`TL;DR:`Both provide equivalent solutions for most cases,but using Objects over Map is more idiomatic across the javascript community and you get simpler api to use. But if you find a use case where you need to use Map, then by all means, use Map.


