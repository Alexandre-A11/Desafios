[See on Website](https://www.codewars.com/kata/523f5d21c841566fde000009)

# Array.diff | Codewars

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list `a`, which are present in list `b` keeping their order.

```
array_diff({1,2}, 2, {1}, 1,*z)=={2} (z==1)
```

```
arrayDiff([1,2],[1]) ==[2]
```

```
array_diff([1,2],[1]) ==[2]
```

```
array_diff([1,2],[1]) ==[2]
```

```
array_diff([1,2],[1]) ==[2]
```

```
arrayDiff([1,2],[1])==[2]
```

```
difference[1,2] [1]==[2]
```

```
Kata.ArrayDiff(newint[] {1,2}, newint[] {1}) =>newint[] {2}
```

```
arrayDiff[|1|] [|1;2|]=[|2|]
```

```
array_diff(vec![1,2], vec![1]) ==vec![2]
```

```
(=(array-diff[12][1])[2])
```

```
Kata.arrayDiff([1,2],[1]) ==[2]
```

```
Kata.arrayDiff(newint[] {1,2}, newint[] {1}) =>newint[] {2}
```

```
arraydiff([1,2],[1]) ==[2]
```

```
arrayDiff(@[1,2],@[1]) == @[2]
```

```
arrayDiff([1,2],[1]) ==[2]
```

```
array_diff(c(1,2), 1)==2
```

```
array_diff([1,2],[1],[2]). % Result = [2]
```

```
arrayDiff(Seq(1,2), Seq(1)) ==Seq(2)
```

If a value is present in `b`, all of its occurrences must be removed from the other:

```
array_diff({1,2,2,2,3}, 5, {2}, 1,*z)=={1,3} (z==2)
```

```
arrayDiff([1,2,2,2,3],[2]) ==[1,3]
```

```
array_diff([1,2],[1]) ==[2]
```

```
array_diff([1,2,2,2,3],[2]) ==[1,3]
```

```
arrayDiff([1,2,2,2,3],[2])==[1,3]
```

```
difference[1,2,2,2,3] [2]==[1,3]
```

```
Kata.ArrayDiff(newint[] {1,2,2,2,3}, newint[] {2}) =>newint[] {1,3}
```

```
arrayDiff[|2|] [|1;2;2;2;3|]=[|1;3|]
```

```
array_diff(vec![1,2,2,2,3], vec![2]) ==vec![1,3]
```

```
(=(array-diff[1,2,2,2,3][2])[1,3])
```

```
Kata.arrayDiff([1,2,2,2,3],[2]) ==[1,3]
```

```
Kata.arrayDiff(newint[] {1,2,2,2,3}, newint[] {2}) =>newint[] {1,3}
```

```
arraydiff([1,2,2,2,3],[2]) ==[1,3]
```

```
arrayDiff(@[1,2,2,2,3],@[2]) == @[1,3]
```

```
arrayDiff([1,2,2,2,3],[2]) ==[1,3]
```

```
array_diff(c(1,2,2,2,3), 2)==c(1,3)
```

```
array_diff([1,2,2,2,3],[2],[1,3]).
```
