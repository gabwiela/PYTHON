'''
Peça ao usuário para inserir dois números. Use .format() para exibir uma mensagem que mostre a soma, subtação, multiplicação e divisão desses números com duas casas decimais.
'''

numero1 = float(input('Digite um número: '))
numero2 = float(input("Digite outro número: "))
soma = numero1 + numero2
subtra = numero1 - numero2
multi = numero1 * numero2
divi = numero1 / numero2

print("A soma dos dois números é: {}".format(soma))
print('A subtração desses números é: {}'.format(subtra))
print("A multiplicação desses números é: {}".format(multi))
print("A divisão desses números é: {}".format(divi))
