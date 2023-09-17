# source: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/largest-number-10-ca319b09/

# Print the largest possible number which can be built from given N number after removing K digits from it
# Sample Input
# 3412 1
# Sample Output
# 412

from itertools import combinations

# Solution 1

# # Input string
# n = input()
#
# # Number of characters to be removed from n string
# k = int(input())
#
# print(max([int("".join(combo)) for combo in combinations(n, len(n) - k)]))

# Solution 2
    n, k = input().split(' ')
    print(max([int("".join(combo)) for combo in combinations(n, len(n) - int(k))]))
