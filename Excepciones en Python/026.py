lista=[2,4]

try:
    print(lista[1])
except IndexError:
    print("Error: error en el índice")
else:
    print("No hay error")
finally:
    print("Se ejecutó")