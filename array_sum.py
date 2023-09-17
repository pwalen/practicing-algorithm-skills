# source: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/array-sum-2-725368ac/discussion/solution-using-pytho-1a118f9a/

# Sample Input (integers)
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005

# Sample Output
# 5000000015

# Solution 1
n = int(input())
print(sum(list(map(int, input().split()))))

# Solution 2
n = int(input())
print(sum([int(x) for x in input().split()]))
