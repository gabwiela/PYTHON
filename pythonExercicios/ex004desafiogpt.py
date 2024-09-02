'''
Escreva um programa que peça ao usuário uma medida em metros. Use .format() para exibir essa medida convertida em centímetros, milímetros e quilômetros, com uma mensagem apropriada para cada conversão.
'''

metros = float(input("Digite o valor em metros: "))

centi = metros * 100
mili = metros * 1000
km = metros / 1000

print("O valor convertido para centímetro é de {}".format(centi))
print("O valor convertido para milímetros é de {}".format(mili))
print("O valor convertido para quilômetros é de {}".format(km))
