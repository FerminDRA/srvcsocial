def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    great=[]
    for l in L:
        great.append(l>thresh)
    return great
l=[1, 2, 3, 4]
print(elementwise_greater_than(l,5))
print(elementwise_greater_than(l,2))