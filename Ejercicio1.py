
print(f'---Digita 1 para agregar a un ciclista---')
print(f'---Digita 2 para ver los resultados---')
print(f'---Digita 3 para salir---')

def calcular_ciclista_rapido():
    ciclistas = []
    tiempoMenor = 100
    opcion = 100
    while opcion != 3:
        ciclista = {}
        opcion = int(input("Digite la opción que desee"))
        if opcion == 1:
            nombre = input("Digite el nombre del ciclista: ")
            edad = int(input("Digite la edad: "))
            pais = input("Digite el pais: ")
            minutos = int(input("Digite los minutos que se demoro: "))
            ciclista['nombre'] = nombre
            ciclista['edad'] = edad
            ciclista['pais'] = pais 
            ciclista['minutos'] = minutos
            ciclistas.append(ciclista)
        elif opcion == 2:
            for i in ciclistas:
                if(i['minutos'] < tiempoMenor):
                    tiempoMenor = i['minutos']
            print(f'El tiempo mas rapido fue{tiempoMenor}')

calcular_ciclista_rapido()

