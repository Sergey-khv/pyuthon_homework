def square(side):
    area = side * side
    if area == int(area):
        return int(area)
    else:
        return int(area) + 1


side1 = 5
side2 = 3.5
side3 = 4.2

print(f"Сторона: {side1}, площадь: {square(side1)}")
print(f"Сторона: {side2}, площадь: {square(side2)}")
print(f"Сторона: {side3}, площадь: {square(side3)}")
