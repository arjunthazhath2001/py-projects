import random
names=["a","b","c"]

marks= {name:random.randint(60,90) for name in names}

passed= {name:mark for name,mark in marks.items() if mark>67}

print(marks)
print(passed)
