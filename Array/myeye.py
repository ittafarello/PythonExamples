from pip._vendor.distlib.compat import raw_input

n = int(raw_input().strip())
m = int(raw_input().strip())
k = int(raw_input().strip())
a = [[0] * m for i in range(n)]
z = abs(k) + 0
getin = True
for rows, value in enumerate(a):
    # if k -1 negative then check to x
    # otherwise evaluate all expressions
    if k < 0:
        getin = False
        w = k + (rows + abs(k))
        if w >= abs(k):
            getin = True
    if getin:
        for cols in range(m):
            if z == cols:
                a[rows][cols] = 1
                z = z + 1
                break
print(a)
