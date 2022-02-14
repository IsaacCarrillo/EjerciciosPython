#Programa para modificar errores de salida

print("Ingresa el no de astronautas")
astronautas = int(input ())

print("Ingresa la cantidad de agua restante (Lts)")
aguares = int(input ())

print("Ingresa los dias restantes")
dias = int(input ())

print("Llama la funcion water_left() para saber alcanzan los suministros")

def water_left():
    daily_usage = astronautas * 11
    total_usage = daily_usage * dias
    total_water_left = aguares - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronautas} astronautas despues de {dias} days!")
    return f"Agua total despues de {dias} dias es: {total_water_left} litros"

input("Presiona cualquier tecla para salir")

