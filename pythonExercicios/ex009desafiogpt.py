'''Insira a marca, modelo e o ano de fabricação de um carro'''

nome = input("Qual a marca do carro? ")
anof = input("Seu ano de fabricação: ")
fabc = input("Digite a fabricação do carro: ")

m = "O carro é da marca {}, chamada {} do ano {}".format(nome, anof, fabc)

print(m)