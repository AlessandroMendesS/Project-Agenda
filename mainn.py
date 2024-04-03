def multiplicacao(num1,num2):
    resultado = num1 * num2
    print('Resultado da multiplição: {}'.format(resultado))

if __name__ == "main":
    permanece = True

while permanece:
    try:
        num1 = int(input('Informe o primerio numero: '))
        num2 = int(input('Informe o segundo numero: '))
        permanece = False
    except ValueError:
        print('Entrada Invalida.Certifique-se de inserir numeros validos.')

multiplicacao(num1,num2)