motorcycles = ['honda','yamha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

newmotor = []
for motor in motorcycles:
	newmotor.append(motor)
newmotor.insert(0,'heihei')
print(newmotor)
#del newmotor[1]
print(newmotor)

popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('ducati')
print(motorcycles)