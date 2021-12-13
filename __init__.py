# Variáveis
verificadorDeTamanho = 0
soma = 0

# Verificar se os números digitados tem exatamente os 11 dígitos do CPF
while verificadorDeTamanho != 11:
    cpf = input('Digite um CPF válido(11 números): ')
    verificadorDeTamanho = len(cpf)

# Fazer a soma dos 9 primeiros dígitos do CPF e multiplicar por 10
for p, r in enumerate(range(10, 1, -1)):
    soma += 10 * (int(cpf[p]) * r)

# Verificar se o resto da variável soma dividido por 11 é igual ao décimo dígito do CPF
# Se não for o CPF será inválido
if not (soma % 11 == int(cpf[9])):
    print('CPF INVÁLIDO!!!')
else:
    soma = 0
    for p, r in enumerate(range(11, 1, -1)): # Fazer a soma dos 10 primeiros dígitos do CPF e multiplicar por 10
        soma += 10 * (int(cpf[p]) * r)
# Verificar se o resto da variável soma dividido por 11 é igual ao décimo primeiro dígito do CPF
# Se não for o CPF será inválido
    if not (soma % 11 == int(cpf[10])):
        print('CPF INVÁLIDO!!!')
    else:
        print('CPF VÁLIDO!!!')

"""
-Falta
* Implementar as excessões dos CPFS válidos
* Implementar uma repetição até ser inserido um CPF válido
* Implentar por modo procedural
* Implentar por orientação a objeto
* No fim uma interface
"""