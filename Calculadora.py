"Calculadora.py"
#Calculadora criada com a Linguagem de Programação Python


primeironumero = input('Digite o Primeiro Número:')
operador = input('Digite o Operador:')
segundonumero = int(input('Digite o Segundo Número:'))

if operador == '+':
    resultado = int(primeironumero) + int(segundonumero)
if operador == '-' :
    resultado = int(primeironumero) - int(segundonumero)
if operador == '*':
    resultado = int(primeironumero) * int(segundonumero)
if operador == '/':
    resultado = int(primeironumero) / int(segundonumero)
print('O resultado da operação é: ' + str(resultado))

 