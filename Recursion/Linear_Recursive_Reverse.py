# Sequence reverse recursively O(n).
def reverese(S,start,stop):
    if start < stop-1: #if start is not empty and has not only one element.
        S[start],S[stop-1] = S[stop-1],S[start]
        reverese(S, start+1,stop-1) # recur in rest.
        return S
S = [1,2,3,4,5]
start = 0
stop = S[-1]
print(S[stop-1])
print(reverese(S,start,stop))
