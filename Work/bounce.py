# bounce.py
#
# Exercise 1.5
height = 100
i = 1
while( i <= 10):
    newHeight = (3/5)*height
    # round to 4 digits
    # print(i, round(newHeight, 4))
    print(i, newHeight)
    height = newHeight
    i = i + 1
