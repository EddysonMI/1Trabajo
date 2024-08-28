
data = [
    {'Nombre': 'Juan', 'Edad': 15, 'Nota': 8.5},
    {'Nombre': 'Ana', 'Edad': 14, 'Nota': 9.0},
    {'Nombre': 'Luis', 'Edad': 16, 'Nota': 7.5},
    {'Nombre': 'Marta', 'Edad': 15, 'Nota': 8.0}
]


print("Datos iniciales:")
for student in data:
    print(student)



#actualizacion 
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla"]

for i, student in enumerate(data):
    student['Ciudad'] = ciudades[i]

print("\nDataFrame actualizado:")
for student in data:
    print(student)
