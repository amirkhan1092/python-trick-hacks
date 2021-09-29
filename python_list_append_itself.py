"""
By appending a list to itself, you create a self-referencing list. This is denoted by the ellipsis ([...]). It's like a recursive function (without a break condition).

list1 = [1, 2, 3]
list1.append(list1)

print(list1) # [1, 2, 3, [...]]

When you "zoom in" on the self-referencial fourth list item, you get the same list again:

print(list1[3]) # [1, 2, 3, [...]]

And this list slice's fourth element is the same as the original list again:

print(list1[3][3]) # [1, 2, 3, [...]]

You could do this forever and would always get the same result. So this is a lot like one of these fractal images.


In your example, it's [1,2,[...]] and not [1,2,1,2] because you append a reference to itself to the same list again.

Instead of saying

a = [1,2]
a.append([1, 2]),

you say

a = [1,2]
a.append(a)

which leads to the above-mentioned "recursive" effect. Another way to actually append [1, 2] to the list would be

a = [1,2]
a.append(a[:])

print(a) # [1, 2, [1, 2]]
"""


