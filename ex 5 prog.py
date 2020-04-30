num = int(input("Digite a quantidade de números: "))

for n in range(num):
    numero = int(input("Digite um número para saber o seu Fatorial: ") )

    resultado=1
    for n in range(1,numero+1):
        resultado *= n

    print("O fatorial do número digitado é:",resultado)

    