For this problem, I used:
- `List` to store [queue] 
- `Dict` to store [cache]

# About get method:
I used remove, insert method of `list` to update this element to be newest of the [queue] and `dict` get method to retrive the element data

# About set method:
I checked 2 case:
- `key` not in cache:
- - insert new object to `cache`
- - check if not out of memory (length of `queue`) => insert `key` to `queue`
- - check if out of memory (length of `queue`) 
    => remove last element
    => insert `key` to `queue`
- `key` in cache:
    => update this element to be newest of the [queue]

Time and Space Complexities:
- Time: O(1) with get/set operation
- Space: O(n) in the worst-case