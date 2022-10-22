numerouno= int(input("Ingrese un número: "))
numerodos= int(input("Ingrese un número: "))

respuesta1 = lambda : 1 if numerouno > numerodos else -1

respuesta = lambda : f'El {numerouno} es mayor que {numerodos}' if numerouno < numerodos else f'El {numerouno} es mayor que {numerodos}'

1