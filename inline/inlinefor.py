q = [1, 2, 3]
vm = [0, 0, 2, 0]
p = [q.index(v) if v in q else False for v in vm]
print(p)
