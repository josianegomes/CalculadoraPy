while True:
    try:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        break
    except ValueError:
        print('Digite somente números!')

print('Selecione a operação aritmética')

operacao = int((input('1-somar \n'
                      '2-subtrair \n'
                      '3-multiplicar \n'
                      '4-dividir \n')))

if operacao == 1:
    print('Resultado da soma é {} + {} é igual a {}'.format(n1, n2, n1 + n2))

if operacao == 2:
    print('Resultado da subtração é {} - {} é igual a {}'.format(n1, n2, n1 - n2))

if operacao == 3:
    print('Resultado da multiplicação é {} * {} é igual a {}'.format(n1, n2, n1 * n2))

if operacao == 4:
    try:
         print('Resultado da divisão é {} / {} é igual a {}'.format(n1, n2, n1 / n2))
    except ZeroDivisionError:
        print('não é possível dividir por zero')

else:
    print('Nenhuma das opções são válidas.')
