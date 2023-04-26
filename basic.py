# 1. get duplicates from an array
array = [1, 2, 3, 3, 3, 4, 5, 3, 3, 6, 3, 5]
dup = []
for i, el in enumerate(array):
    if array.count(el) > 1:
        if el not in dup:
            dup.append(el)
