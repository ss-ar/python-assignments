def area_of_circle(r):
    pi = 3.14
    result = pi*r*r
    return result

def circumference(d):
    pi = 3.14
    result = pi*d
    return result

def perimeter_rectangle(l,w):
    perimeter = 2*(l+w)
    return perimeter

length = 8
width = 4
diameter = 12
circum = circumference(diameter)
area = area_of_circle(6)
perimeter = perimeter_rectangle(length,width)

print(area)
print(circum)
print(perimeter)

