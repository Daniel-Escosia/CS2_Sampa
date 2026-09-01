import time
import math

print("DISTANCE FINDER V.1")
time.sleep(0.5)
print("Put the format of your coordinate as X,Y, no spaces.")
# Input.
a = input("Coordinate 1 = ")
b = input("Coordinate 2 = ")

# Splitting the input, 0 for the first value (X) and 1 for the second (Y)
# float turns the string to a float, meaning it can be subtracted and added to each other.
x1 = float(a.split(",")[0])
x2 = float(b.split(",")[0])
y1 = float(a.split(",")[1])
y2 = float(b.split(",")[1])

# Pythagorean Theorem and output.
# sqrt sqaureroots the entire thing, while pow provides the power of 2 in the equation.
dist = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
print("The distance is ", dist)

# < REFLECTION >
## The math library simplified my program through making it so that we do not have to manually put each value, each operation and complex mathematical expressions.
## Square roots were easier to use, rather than getting it manually. The power function reduced the size of each value by alot.
## It would really take alot of lines to produce a square root, nonetheless powers.
