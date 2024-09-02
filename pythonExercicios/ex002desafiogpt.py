'''
Crie uma programa que peça ao usuário o nome de um produto, sua quantidade e seu preço unitário. Use '.format()' para exibir uma mensagem que mostre o nome do produto, a quantidade comprada e o custo total (quantidade*preço unitario).
'''

nomeproduto = input("Qual produto você deseja? ")
quant = float(input("Qual a quantidade desejada: "))
punit = float(input("Digite o preço: "))

custototal = quant * punit

print("=======MC DONALDS ANTONIO BARRETO======")
print("O produto escolhido foi: {}".format(nomeproduto))
print("A quantidade comprada pelo cliente foi de {} unidades".format(quant))
print("O custo total desta compra é de {} reais".format(custototal))
print('====OBRIGADO PELA COMPRA, VOLTE SEMPRE======')