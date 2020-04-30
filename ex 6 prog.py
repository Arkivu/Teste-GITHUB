func = int(input("Digite a quantidade de empregados: "))
cont = 1
for n in range(func):
    
    nome_func = str(input("Digite o nome do funcionario: "))
    sal_func = float(input("Digite o salario do funcionario: "))
    media = 0

    if sal_func >=3000:
        sal_func = sal_func +(sal_func*(8/100))
        media = media+sal_func*1.08
    elif sal_func >=2000 and sal_func <3000:
        sal_func = sal_func +(sal_func*(10/100))
        cont +=1
        media = media+sal_func*1.10
    else:
        sal_func = sal_func +(sal_func*(12/100))
        media = media+sal_func*1.12
    
    
    print("O novo salárido do(a)",nome_func,"é:",sal_func)

print("Quantidade de funcionarios que receberam 10% de aumento:",cont-1)
print("Salário médio dos funcionários (após reajuste): ", media)