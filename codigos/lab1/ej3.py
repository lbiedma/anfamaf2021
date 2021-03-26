import math
x = 2.0
i = 1

while not math.isinf(x*2):
	x = x*2
	i = i+1

print(f"La mayor potencia de 2 en punto flotante es = {x}")
print("Su exponente es:",i)

x = 2.0
i = 1

while x/2 != 0:
	x = x/2
	i = i-1

print("La menor potencia de 2 en punto flotante es:",x)
print("Su exponente es:",i)
