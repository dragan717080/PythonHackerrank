from math import sqrt, asin, acos, atan, degrees

ab, bc = int(input()), int(input())
ac = sqrt(ab**2 + bc**2)

# Calculating mc and mb is not needed

# Opposite: ab, adjacent:  bc, hypotenuse: ac

# Using SOH
print(f"{round(degrees(asin(ab / ac)))}{chr(176)}")
# Using CAH
print(f"{round(degrees(acos(bc / ac)))}{chr(176)}")
# Using TOA
print(f"{round(degrees(atan(ab / bc)))}{chr(176)}")
