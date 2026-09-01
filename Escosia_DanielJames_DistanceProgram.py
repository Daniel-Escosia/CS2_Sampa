import time
import math

print("DISTANCE FINDER V.1")
time.sleep(0.5)
print("Put the format of your coordinate as X,Y, no spaces.")
a = input("Coordinate 1 = ")
b = input("Coordinate 2 = ")
x1 = float(a.split(",")[0])
x2 = float(b.split(",")[0])
y1 = float(a.split(",")[1])
y2 = float(b.split(",")[1])
   
dist = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
print("The distance is ", dist)

# < REFLECTION >
## The math library simplified my program through making it so that we do not have to manually put each value, each operation and complex mathematical expressions.
## Square roots were easier to use, rather than getting it manually. The power function reduced the size of each value by alot.
## It would really take alot of lines to produce a square root, nonetheless powers.