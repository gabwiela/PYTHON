#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = int(input("Qual o preço do produto? "))

desc = preco * 0.5

print("O preço original é de {} reais mas com o desconto de 5% fica {} reais".format(preco, desc))