# String Split and Join | HackerRank

[](https://www.hackerrank.com/challenges/python-string-split-and-join/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign)

In Python, a string can be split on a delimiter.

**Example:**

```
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings.
>>> print a
['this', 'is', 'a', 'string']

```

Joining a string is simple:

```
>>> a = "-".join(a)
>>> print a
this-is-a-string

```

**Task**

You are given a string. Split the string on a `" "` (space) delimiter and join using a `-` hyphen.

**Function Description**

Complete the _split_and_join_ function in the editor below.

_split_and_join_ has the following parameters:

-   _string line:_ a string of space-separated words

**Returns**

-   _string:_ the resulting string

**Input Format**

The one line contains a string consisting of space separated words.

**Sample Input**

```
this is a string

```

**Sample Output**

```
this-is-a-string
```
