# HackerRank Question - Optimizing Box Weights (example question)

[](https://www.hackerrank.com/test/63ek10mhil5/questions/24i33a0pf0l)

1. Optimizing Box Weights (example question)
   ============================================</section><section class="question-view__instruction">

An Amazon Fulfillment Associate has a set of items that need to be packed into two boxes.Given an integer array of the item weights (`arr`) to be packed, divide the item weights into two subsets, A andB, for packing into the associated boxes, while respecting the following conditions:

-   The intersection of A and B is null.
-   The union A and B is equal to the original array.
-   The number of elements in subset A is minimal.
-   The sum of A's weights is greater than the sum of B's weights.

Return the subset A in increasing order where the sum of A's weights is greater than the sum of B's weights. If more than one subset A exists, return the one with the maximal total weight.

**Example**

_n = 5_

_arr = [3, 7, 5, 6, 2]_

The 2 subsets in _arr_ that satisfy the conditions for *A*are* [5, 7]* and _ [6, 7]_:

-   A is minimal (size 2)
-   Sum(A) = (5 + 7) = 12 > Sum(B) = (2 + 3 + 6) = 11
-   Sum(A) = (6 + 7) = 13 > Sum(B) = (2 + 3 + 5) = 10
-   The intersection of A and B is null and their union is equal to _arr_.
-   The subset A where the sum of its weight is maximal is [6,7].

**Function Description**

Complete the *minimalHeaviestSetA*function in the editor below.

\*minimalHeaviestSetA **\*has the following parameter(s):**
_int arr[]:_ an integer array of the weights of each item in the set

**Returns:**
**_int[]_ : an integer array with the values of subset A**

**Constraints**

-   _1 ≤ n ≤ 105_
-   *1 ≤ arr[i]≤ 105\*\*\*\*(*where\* 0 ≤ i < n)\*\*\*

<!--       <StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details open=""><summary class="section-title">**Input Format For Custom Testing**</summary>

**The first line contains an integer, _n,_ denoting the number of elements in the array.**

**Each line _i_ of the _n_ subsequent lines contains an integer, which is an element of _arr._**

</details>
<!--        </StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details open=""><summary class="section-title">**Sample Case 0**</summary>

Sample Input For Custom Testing

STDIN Function

---

**6 **→* arr*[] size n = 6**
5 **→* arr*[] = **[5, 3, 2, 4, 1, 2]\*\***
3
2
4
1
2\*\*

Sample Output

4
5

Explanation

**_n = 6_**

**_arr = [5, 3, 2, 4, 1, 2]_**

The subset of A that satisfies the conditions is [4, 5] :

-   A is minimal (size 2)
-   Sum(A) = (4 + 5) = 9 > Sum(B) = (1 + 2 + 2 + 3) = 8
-   The intersection of A and B is null and their union is equal to _arr._
-   The subset A with the maximal sum is [4, 5].

</details>

<details open=""><summary class="section-title">**Sample Case 1**</summary>

Sample Input For Custom Testing

STDIN Function

---

**5**→ arr[] size n = 5**
4**→ arr[] = **[4, 2, 5, 1, 6]
2
5
1
6**

Sample Output

5
6

Explanation

**_n = 5_**

**_arr = [4, 2, 5, 1, 6]_**

The subset of A that satisfies the conditions is [5, 6]:

-   A is minimal (size 2)
-   Sum(A) = (5 + 6) = 11> Sum(B) = (1 + 2 + 4) = 7
-   Sum(A) = (4 + 6) = 10> Sum(B) = (1 + 2 + 5) = 8
-   The intersection of A and B is null and their union is equal to _arr_.
-   The subset A with the maximal sum is [5, 6].
