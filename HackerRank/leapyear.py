from pip._vendor.distlib.compat import raw_input


def is_leap(year):
    y4 = year % 4 == 0
    print(year % 4)
    y100 = year % 100 == 0
    print(year % 100)
    y400 = year % 400 == 0
    print(year % 400)
    print(f"y4 {y4} y100 {y100}  y400 {y400}")
    leap = False
    if y4:
        leap = True
        if y100:
            leap = False
            if y400:
                leap = True


    return leap


year = int(raw_input().strip())
print(is_leap(year))
