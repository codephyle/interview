"""
FRUITS INTO BASKETS

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Examples

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
             If we had started at the first tree, we would only pick from trees [0,1].

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
             If we had started at the first tree, we would only pick from trees [1,2].

Note: Alternatively, the trees are provided as char array. 
    str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']) => 3  [2 'C's and and one 'A'] 
    str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']) => 5 
"""
# https://leetcode.com/problems/fruit-into-baskets/
from collections import defaultdict


def totalFruit(fruits):
    start = 0
    maxTotal = 0
    fruitCount = defaultdict(int)
    for end, fruit in enumerate(fruits):
        fruitCount[fruit] += 1
        while len(fruitCount) > 2:
            fruitCount[fruits[start]] -= 1
            if fruitCount[fruits[start]] == 0:
                del fruitCount[fruits[start]]
            start += 1
        maxTotal = max(maxTotal, end - start + 1)
    return maxTotal

assert totalFruit([1,2,1]) == 3
assert totalFruit([1,2,3,2,2]) == 4
assert totalFruit([0,1,2,1,1,2]) == 5
assert totalFruit(['A', 'B', 'C', 'B', 'B', 'C']) == 5 
