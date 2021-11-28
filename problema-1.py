import math

DECIMAL_PRECISION = 4 

a = float(input("intruduza a: "))
b = float(input("intruduza b: "))
c = float(input("intruduza c: "))

root_1 = (-b + math.sqrt((-b)**2 -4*a*c))/(2*a)
root_2 = (-b - math.sqrt((-b)**2 -4*a*c))/(2*a)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"raiz 1 = {round(root_1, DECIMAL_PRECISION)}")
print(f"raiz 2 = {round(root_2, DECIMAL_PRECISION)}")