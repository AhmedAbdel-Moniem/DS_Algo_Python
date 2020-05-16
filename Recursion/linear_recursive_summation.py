# Recursive linear Sum  O(n).
def linear_sum(s,n):
    if n == 0:
        return 0
    else:
        return linear_sum(s,n-1) + s[n-1]

s = [4, 3, 6, 2, 8]
print(linear_sum(s,5))
