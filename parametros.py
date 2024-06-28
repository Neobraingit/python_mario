
import argparse

parse = argparse.ArgumentParser(description='Suma de dos números')
parse.add_argument('Número1', type=int, help='Primer número')
parse.add_argument('Número2', type=int, help='Segundo número')

argumentos = parse.parse_args()

numero1 = argumentos.Número1
numero2 = argumentos.Número2
resultado = numero1 + numero2

print (f'El primer número es {numero1} y el segundo número es {numero2}')
print ('El resultado es: ', resultado)