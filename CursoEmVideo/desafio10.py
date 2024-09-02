#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$ 3,27.

dindin = float(input("Quanto você tem na carteira? "))

taxa_cambio = 3.27
dolar = int(dindin / taxa_cambio)


print("Com {} reais você pode comprar {} dolares".format(dindin,dolar))