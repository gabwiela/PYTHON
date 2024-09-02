#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

av1 = float(input("Digite sua nota da primeira avaliação: "))
av2 = float(input("Digite a nota da segunda avaliação: "))

media = (av1 + av2) / 2

mensagem1 = "AV1: {}".format(av1)
mensagem2 = "AV2: {}".format(av2)
mensagem3 = "Média Geral: {}".format(media)

print(mensagem1)
print(mensagem2)
print(mensagem3)